#!/usr/bin/env python3
"""Bounded synthetic check of the transfer-to-archive filesystem handoff."""
import gzip
import json
from pathlib import Path
import resource
import tempfile
import time

from transport import encode, restore, sha, TARGET


def package(root, payload):
    target = {'fixture': 'restore-calibration', 'bytes': len(payload), 'sha256': sha(payload)}
    manifest, chunks = encode(payload, target)
    root.mkdir()
    (root / 'manifest.json').write_text(json.dumps(manifest) + '\n')
    for name, raw in chunks.items():
        (root / name).write_bytes(raw)
    return target


def main():
    start = time.perf_counter()
    results, controls = [], {}
    with tempfile.TemporaryDirectory(prefix='adva-restore-') as tmp:
        root = Path(tmp)
        for i, source in enumerate([b'first independently pinned bytes\n', bytes(range(256)) * 1024]):
            compressed = gzip.compress(source, mtime=0)
            incoming = root / f'incoming-{i}'
            expected = package(incoming, compressed)
            output = root / f'restored-{i}.gz'
            t = time.perf_counter()
            receipt = restore(incoming, output, expected)
            elapsed = (time.perf_counter() - t) * 1000
            assert output.read_bytes() == compressed
            # Independently read the saved gzip with a fixed fixture output cap.
            with gzip.open(output, 'rb') as stream:
                recovered = stream.read(262145)
            assert recovered == source
            results.append({'case': i, 'status': receipt['status'], 'bytes': len(compressed),
                            'sha256': sha(compressed), 'restore_write_sync_readback_ms': elapsed,
                            'synthetic_gzip_recovery': 'Matched', 'original_bytes': len(source)})
            before = output.read_bytes()
            try:
                restore(incoming, output, expected)
            except FileExistsError:
                assert output.read_bytes() == before
                controls[f'existing-output-{i}'] = 'RejectedAndUnchanged'
            else:
                raise AssertionError('existing output overwritten')
            # Tampered transport must fail before any output is created.
            part = incoming / 'part-000.b64'
            old = part.read_bytes()
            part.write_bytes(b'!' + old[1:])
            failed = root / f'failed-{i}.gz'
            try:
                restore(incoming, failed, expected)
            except ValueError:
                assert not failed.exists()
                controls[f'tamper-{i}'] = 'RejectedWithoutOutput'
            else:
                raise AssertionError('tamper accepted')
            part.write_bytes(old)
            try:
                restore(incoming, failed, TARGET)
            except ValueError:
                assert not failed.exists()
                controls[f'real-pin-{i}'] = 'RejectedWithoutOutput'
            else:
                raise AssertionError('synthetic bytes promoted to real target')
        # A symlink is an existing destination and must not replace its referent.
        victim = root / 'victim'; victim.write_bytes(b'keep')
        link = root / 'link.gz'; link.symlink_to(victim)
        try:
            restore(incoming, link, expected)
        except FileExistsError:
            assert link.is_symlink() and victim.read_bytes() == b'keep'
            controls['symlink-output'] = 'RejectedAndUnchanged'
        else:
            raise AssertionError('symlink destination accepted')
    elapsed = (time.perf_counter() - start) * 1000
    assert elapsed < 5000
    print(json.dumps({'schema': 'adva.restore-calibration.proposed', 'version': 0,
                     'status': 'SyntheticRestoreChecked', 'results': results, 'controls': controls,
                     'real_artifact': 'NotReceived', 'complete_archive_status': 'Unknown',
                     'native_replay': 'NotRun', 'mathematical_discharges': 0,
                     'wall_ms_before_report': elapsed,
                     'process_peak_rss_kib_linux': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                     'budget': {'timeout_seconds': 5, 'fixtures': 2, 'refusal_controls': 7,
                                'gzip_fixture_output_cap': 262145},
                     'unmeasured': ['authoring', 'retrieval', 'report serialization'],
                     'residual': 'Real artifact and full archive were not verified; crash and disk-full injection not performed'}, indent=2))


if __name__ == '__main__':
    main()
