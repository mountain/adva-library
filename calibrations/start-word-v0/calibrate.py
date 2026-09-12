#!/usr/bin/env python3
"""One bounded typed entry word Start calibration; preserves exact inputs."""
import copy
import json
import resource
import sys
import time

from start_word import build, check, digest, encode


def run():
    start = time.perf_counter()
    checks = 0
    verification_ms = 0

    def execute(inputs):
        nonlocal checks, verification_ms
        checks += 1
        if checks > 32 or time.perf_counter() - start > 5:
            raise RuntimeError('Unknown: run budget exhausted')
        t = time.perf_counter()
        result = check(*(None if inputs[k] is None else inputs[k].encode('utf-8')
                         for k in ['source_utf8', 'policy_utf8', 'witness_utf8']),
                       inputs['expected_source_sha256'], inputs['expected_policy_sha256'])
        verification_ms += (time.perf_counter() - t) * 1000
        return result

    cases = []
    formation_ms = 0
    for label, m, n, value in [('first', 3, 4, 5), ('reuse', 5, 7, 17)]:
        t = time.perf_counter()
        source = {'schema': 'adva.disclosed-integer-record.v0', 'record_label': label, 'value': value}
        policy = {'schema': 'adva.residue-projection-policy.v0', 'moduli': [m, n], 'interval': [0, m*n]}
        sb, pb = encode(source), encode(policy)
        wb = build(sb, pb)
        inputs = {'source_utf8': sb.decode(), 'policy_utf8': pb.decode(), 'witness_utf8': wb.decode(),
                  'expected_source_sha256': digest(sb), 'expected_policy_sha256': digest(pb)}
        formation_ms += (time.perf_counter() - t) * 1000
        judgment = execute(inputs)
        assert judgment['status'] == 'StartWordChecked'
        assert judgment['typed_boundary'] == {'domain_ports': ['source', 'policy'],
                                              'codomain_ports': ['r0', 'r1']}
        assert judgment['ports'] == [value % m, value % n]
        assert judgment['observations'] == [value % m, value % n]
        controls = []
        mutations = ['false-remainder', 'false-quotient', 'noncanonical-remainder',
                     'missing-row', 'duplicate-row', 'reordered-rows', 'replace-source-and-witness',
                     'replace-policy-and-witness', 'equal-value-other-record', 'outside-domain-alias',
                     'missing-source', 'boolean-value']
        for name in mutations:
            changed = copy.deepcopy(inputs)
            w, s, p = json.loads(wb), dict(source), copy.deepcopy(policy)
            reason, status = '', 'Rejected'
            if name == 'false-remainder':
                w['rows'][0]['remainder'] = (w['rows'][0]['remainder'] + 1) % m
                reason = 'DivisionEquation'
            elif name == 'false-quotient':
                w['rows'][0]['quotient'] += 1
                reason = 'DivisionEquation'
            elif name == 'noncanonical-remainder':
                w['rows'][0]['quotient'] -= 1
                w['rows'][0]['remainder'] += m
                reason = 'DivisionRange'
            elif name == 'missing-row':
                w['rows'].pop()
                status, reason = 'Unknown', 'ObservationCoverage'
            elif name == 'duplicate-row':
                w['rows'][1] = dict(w['rows'][0])
                reason = 'DuplicateSlot'
            elif name == 'reordered-rows':
                w['rows'].reverse()
                reason = 'RowOrder'
            elif name == 'replace-policy-and-witness':
                p['moduli'].reverse()
                changed['policy_utf8'] = encode(p).decode()
                w = json.loads(build(sb, encode(p)))
                reason = 'PolicyPinMismatch'
            elif name == 'missing-source':
                changed['source_utf8'] = None
                status, reason = 'Unknown', 'InputUnavailable'
            else:
                if name == 'replace-source-and-witness':
                    s['value'] = 9 if label == 'first' else 3
                    reason = 'SourcePinMismatch'
                elif name == 'equal-value-other-record':
                    s['record_label'] += '-other'
                    reason = 'SourcePinMismatch'
                elif name == 'outside-domain-alias':
                    s['value'] += m*n
                    reason = 'SourceOutsideDomain'
                else:
                    s['value'] = True
                    reason = 'SourceInteger'
                changed_source = encode(s)
                changed['source_utf8'] = changed_source.decode()
                w = json.loads(build(changed_source, pb))
                if name in ['outside-domain-alias', 'boolean-value']:
                    changed['expected_source_sha256'] = digest(changed_source)
            changed['witness_utf8'] = encode(w).decode()
            observed = execute(changed)
            assert observed['status'] == status and observed['reason'] == reason, (name, observed)
            controls.append({'mutation': name, 'inputs': changed, 'judgment': observed})
        cases.append({'label': label, 'inputs': inputs, 'judgment': judgment, 'controls': controls})
    t = time.perf_counter()
    serialized = json.dumps(cases)
    replay_cases = json.loads(serialized)
    serialization_ms = (time.perf_counter() - t) * 1000
    for case in replay_cases:
        assert execute(case['inputs']) == case['judgment']
    return {'schema': 'adva.start-word-calibration.v0', 'status': 'FiniteStartWordChecked',
            'cases': cases, 'checks': checks, 'negative_or_missing_controls': 24,
            'positive_json_replay': 'Matched', 'search_candidates': 0, 'native_calls': 0,
            'formation_ms': formation_ms, 'verification_ms': verification_ms,
            'case_serialization_roundtrip_ms': serialization_ms,
            'wall_ms_before_report': (time.perf_counter() - start) * 1000,
            'process_peak_rss_kib_linux': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform == 'linux' else None,
            'budget': {'checks': 32, 'timeout_seconds': 5, 'bytes_per_input': 4096},
            'unmeasured': ['research and authoring', 'network', 'final report serialization'],
            'residual': ['Caller-side authority for expected pins is assumed, not established',
                         'Physical measurement truth and native source identity are not established',
                         'Disclosed-source baseline; no privacy or acceleration claim',
                         'The word Start adds a typed reading only: no native operation, type, or Seal is created']}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
