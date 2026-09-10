#!/usr/bin/env python3
"""Two reproducible synthetic transfers and bounded refusal controls."""
import base64
import binascii
import copy
import gzip
import hashlib
import json
from pathlib import Path
import resource
import tempfile
import time

from transport import encode, decode, receive, sha, no_duplicate_keys, TARGET


def fixture(seed, size):
    return b''.join(hashlib.sha256(seed.encode() + i.to_bytes(4, 'big')).digest()
                    for i in range((size + 31) // 32))[:size]


def refused(fn):
    try:
        fn()
    except (ValueError, binascii.Error):
        return 'Rejected'
    raise AssertionError('control unexpectedly accepted')


def run():
    start = time.perf_counter()
    records = []
    controls = {}
    for seed, size in [('first-transfer', 180000), ('new-instance-reuse', 260000)]:
        t = time.perf_counter()
        raw = gzip.compress(fixture(seed, size), mtime=0)
        construction_ms = (time.perf_counter() - t) * 1000
        target = {'fixture': seed, 'bytes': len(raw), 'sha256': sha(raw)}
        t = time.perf_counter()
        manifest, chunks = encode(raw, target)
        packaging_ms = (time.perf_counter() - t) * 1000
        t = time.perf_counter()
        assert decode(manifest, chunks, target) == raw
        verification_ms = (time.perf_counter() - t) * 1000
        t = time.perf_counter()
        with tempfile.TemporaryDirectory(prefix='adva-transport-') as tmp:
            directory = Path(tmp)
            (directory / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
            for name, data in chunks.items():
                (directory / name).write_bytes(data)
            assert receive(directory, target) == raw
            replay_ms = (time.perf_counter() - t) * 1000
            (directory / 'unexpected.txt').write_text('extra')
            controls[seed + '/extra-file'] = refused(lambda: receive(directory, target))
        records.append({'fixture': seed, 'uncompressed_bytes': size, 'target': target,
                        'parts': len(chunks), 'status': 'SyntheticPinnedBytesVerified',
                        'construction_ms': construction_ms, 'packaging_ms': packaging_ms,
                        'verification_ms': verification_ms,
                        'filesystem_serialization_and_replay_ms': replay_ms})
        for mutation in ['missing', 'extra', 'duplicate', 'reorder', 'tamper',
                         'invalid-base64', 'wrong-target', 'part-budget', 'raw-budget']:
            m, c, expected = copy.deepcopy(manifest), dict(chunks), dict(target)
            first = m['parts'][0]['name']
            if mutation == 'missing':
                c.pop(first)
            elif mutation == 'extra':
                c['part-999.b64'] = b'x'
            elif mutation == 'duplicate':
                m['parts'][1] = copy.deepcopy(m['parts'][0])
            elif mutation == 'reorder':
                m['parts'].reverse()
            elif mutation == 'tamper':
                c[first] = b'!' + c[first][1:]
            elif mutation == 'invalid-base64':
                c[first] = b'!' + c[first][1:]
                m['parts'][0]['sha256'] = sha(c[first])
            elif mutation == 'wrong-target':
                expected['sha256'] = '0' * 64
                m['target'] = dict(expected)
            elif mutation == 'part-budget':
                m['parts'] = m['parts'] * 65
            else:
                expected['bytes'] = 4 * 1024 * 1024
            controls[seed + '/' + mutation] = refused(lambda: decode(m, c, expected))
    controls['duplicate-json-key'] = refused(
        lambda: json.loads('{"version":0,"version":1}', object_pairs_hook=no_duplicate_keys))
    controls['real-target-not-synthetic'] = refused(lambda: encode(raw, TARGET))
    elapsed = (time.perf_counter() - start) * 1000
    assert elapsed < 5000
    return {'schema': 'adva.text-transport-calibration.proposed', 'version': 0,
            'status': 'SyntheticTransportChecked', 'fixtures': records, 'controls': controls,
            'controls_count': len(controls), 'real_artifact': 'NotReceived',
            'complete_archive_status': 'Unknown', 'native_replay': 'NotRun',
            'mathematical_discharges': 0, 'search_candidates': 0,
            'wall_ms_before_report': elapsed,
            'process_peak_rss_kib_linux': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            'budget': {'process_timeout_seconds': 5, 'fixture_count': 2,
                       'max_parts': 64, 'max_encoded_bytes': 4194304},
            'unmeasured': ['authoring', 'network', 'report serialization'],
            'residual': 'Synthetic reuse tests the transport boundary only; no real native artifact bytes were obtained'}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
