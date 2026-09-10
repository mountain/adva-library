#!/usr/bin/env python3
"""Bounded, external documentary receiver; never executes native artifacts."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import resource
import sys
import time

HERE = Path(__file__).resolve().parent
PEER = 'e0e3433ebcaa2da6ec3e0bc1f67bd316f2c38547'
AUDIT = 'feef303c35ab2d10e3f7763cb0bd73e216e0571e'
LIBRARY = 'f0312ca4a109e8ca26cc01cb678750ad889c95be'
HANDOFF = '059a7e09967326e1030c1c367095aa86be7bd21e1950da85b7c4020803722923'
PINS = {
    'peer-reply.json': '5d7d45364e95cd729fa19b36f31222efe54f4b3593740bd71c7971646c2822f8',
    'peer-report.json': '51694ca9400e5561591832bb9909ae62cbb8ef38274c8b98ba86420e674fd614',
    'text-audit.json': '78f201f8237421945da8c047ae39e4c6d04c8da1cd5957dac2f3383e51417439',
}
PATHS = {
    'peer-reply.json': (PEER, 'experiments/advance_symbol_surface/reply.json'),
    'peer-report.json': (PEER, 'experiments/advance_symbol_surface/evidence/run-01/report.json'),
    'text-audit.json': (AUDIT, 'experiments/symbol_surface_peer_audit/report.json'),
}


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def read(path):
    with path.open('rb') as stream:
        raw = stream.read(65537)
    require(len(raw) <= 65536, 'file budget exceeded')
    return raw


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def bind(reply, report, audit, obligations):
    """Check relation boundaries after separately checking the frozen input bytes."""
    predecessor = dict(repository='mountain/adva-library', commit=LIBRARY,
                       path='symbol-surface/handoff.json', sha256=HANDOFF)
    require(reply['predecessor'] == predecessor, 'wrong predecessor')
    require(report['predecessor_sha256'] == HANDOFF, 'report predecessor mismatch')
    require(reply['evidence']['report_sha256'] == PINS['peer-report.json'], 'wrong report')
    require(reply['observation']['difference'] == report['finding'], 'finding mismatch')
    require(reply['remaining_obligations'] == [x['id'] for x in obligations], 'obligation loss or reorder')
    require(len(obligations) == 9 and all(x['status'] == 'Open' for x in obligations), 'obligation status')
    require(report['native_free'] == 'NotGranted' and
            report['mathematical_proof_admission'] == 'not-granted', 'semantic upgrade')
    require(report['finding']['mathematical_discharges'] == 0 and
            report['finding']['verification_formation'] == 'conditional', 'admission upgrade')
    require(audit['source_commit'] == PEER, 'audit source mismatch')
    require(audit['status'] == 'TextEvidenceChecked' and
            audit['complete_archive_status'] == 'Unknown' and
            audit['native_replay'] == 'NotRun' and
            audit['native_binary_checked'] is False, 'audit scope upgrade')
    require((audit['text_files_checked'], audit['archive_files_declared'],
             audit['remaining_obligations']) == (53, 54, 9), 'coverage mismatch')
    return {
        'schema': 'adva.symbol-surface.receiving-acknowledgment.proposed',
        'version': 0,
        'status': 'RecordedReplyBoundToHandoff',
        'predecessor': predecessor,
        'received_inputs': {name: {'commit': PATHS[name][0], 'sha256': digest}
                            for name, digest in PINS.items()},
        'peer_reported': report['finding'],
        'receiver_checked': 'Pinned text records and their declared relation boundaries',
        'prior_text_audit': 'TextEvidenceChecked',
        'complete_archive_status': 'Unknown',
        'local_native_replay': 'NotRun',
        'native_free': 'NotGranted',
        'mathematical_discharges': 0,
        'remaining_obligations': obligations,
        'exit': 'One finite reception; no polling, execution or automatic continuation',
        'residual': 'Binary bytes, build authentication, native replay and payload mathematics are not checked here',
    }


def run(write):
    start = time.perf_counter()
    pins = json.loads(read(HERE / 'sources.json'))
    require(len(pins) == 3 and {p['local'] for p in pins} == set(PINS), 'source coverage')
    inputs = {}
    for pin in pins:
        name = pin['local']
        raw = read(HERE / name)
        require((pin['commit'], pin['path']) == PATHS[name] and
                pin['repository'] == 'mountain/adva', 'provenance mismatch')
        require(sha(raw) == pin['sha256'] == PINS[name] and
                len(raw) == pin['bytes'], 'input bytes changed')
        inputs[name] = json.loads(raw)
    require(sha(read(HERE.parents[1] / 'handoff.json')) == HANDOFF, 'historical handoff changed')
    raw = read(HERE.parents[1] / 'source/obligations.json')
    require(sha(raw) == '8443a82b97c1e2e0665c4c073f7d9a87095438dc82509d6001c1260b4be34587', 'source obligations changed')
    args = [inputs['peer-reply.json'], inputs['peer-report.json'],
            inputs['text-audit.json'], json.loads(raw)['items']]
    receipt = bind(*args)
    controls = {}
    for name in ['wrong-predecessor', 'missing-obligation', 'archive-upgrade', 'audit-source-mismatch']:
        changed = copy.deepcopy(args)
        if name == 'wrong-predecessor':
            changed[0]['predecessor']['commit'] = '0' * 40
        elif name == 'missing-obligation':
            changed[0]['remaining_obligations'].pop()
        elif name == 'archive-upgrade':
            changed[2]['complete_archive_status'] = 'Complete'
        else:
            changed[2]['source_commit'] = '0' * 40
        try:
            bind(*changed)
        except ValueError as error:
            controls[name] = {'status': 'Rejected', 'reason': str(error)}
        else:
            raise ValueError('control accepted: ' + name)
    # An independently deserialized instance must reproduce the same relation.
    replay = bind(*json.loads(json.dumps(args)))
    require(replay == receipt, 'serialization replay mismatch')
    serial_start = time.perf_counter()
    encoded = json.dumps(receipt, indent=2) + '\n'
    serialization_ms = (time.perf_counter() - serial_start) * 1000
    if write:
        (HERE / 'receipt.json').write_text(encoded)
    else:
        require(json.loads(read(HERE / 'receipt.json')) == receipt, 'stored receipt mismatch')
    elapsed = (time.perf_counter() - start) * 1000
    require(elapsed < 5000, 'five second budget exceeded')
    return {'status': 'ReceivingContractChecked', 'controls': controls,
            'serialization_replay': 'Matched', 'receipt_sha256': sha(encoded.encode()),
            'search_candidates': 0, 'native_invocations': 0,
            'wall_ms_before_report': elapsed, 'receipt_serialization_ms': serialization_ms,
            'process_peak_rss_kib_linux': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform == 'linux' else None,
            'unmeasured': ['authoring', 'retrieval', 'report serialization'],
            'budget': {'wall_seconds': 5, 'max_input_file_bytes': 65536,
                       'input_files': 6, 'relation_controls': 4}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='create the deterministic receipt')
    options = parser.parse_args()
    print(json.dumps(run(options.write), indent=2))
