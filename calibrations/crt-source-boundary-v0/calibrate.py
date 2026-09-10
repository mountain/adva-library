#!/usr/bin/env python3
"""Exact finite counterexample to coprimality implying source fidelity."""
import json
import math
import resource
import sys
import time


def run():
    start = time.perf_counter()
    nodes = 0

    def tick():
        nonlocal nodes
        nodes += 1
        if nodes > 256 or time.perf_counter() - start > 5:
            raise RuntimeError('Unknown: finite budget exhausted')

    def inverse(a, modulus):
        candidates = []
        for k in range(1, modulus):
            tick()
            if a * k % modulus == 1:
                candidates.append(k)
        assert len(candidates) == 1
        return candidates[0]

    records = []
    for m, n, source in [(3, 4, 5), (5, 7, 17)]:
        assert math.gcd(m, n) == 1
        M = m * n
        t = time.perf_counter()
        coefficients = (n * inverse(n, m), m * inverse(m, n))
        construction_ms = (time.perf_counter() - t) * 1000
        t = time.perf_counter()
        fibres = {}
        for x in range(M):
            tick()
            fibres.setdefault((x % m, x % n), []).append(x)
        assert len(fibres) == M and all(len(xs) == 1 for xs in fibres.values())
        for residues, xs in fibres.items():
            computed = sum(a * b for a, b in zip(residues, coefficients)) % M
            assert computed == xs[0]
        honest = (source % m, source % n)
        altered = ((honest[0] + 1) % m, honest[1])
        assert fibres[honest] == [source]
        assert len(fibres[altered]) == 1 and fibres[altered][0] != source
        alias = source + M
        assert (alias % m, alias % n) == honest
        verification_ms = (time.perf_counter() - t) * 1000
        records.append({'moduli': [m, n], 'domain': {'lower_inclusive': 0, 'upper_exclusive': M},
                        'source': source, 'crt_coefficients': list(coefficients),
                        'honest_observation': list(honest), 'honest_fibre': fibres[honest],
                        'altered_observation': list(altered), 'altered_fibre': fibres[altered],
                        'altered_answer_faithful_to_source': False,
                        'outside_domain_alias': alias, 'fully_checked_states': M,
                        'construction_ms': construction_ms, 'verification_ms': verification_ms})
    fibre = []
    for x in range(24):
        tick()
        if (x % 4, x % 6) == (1, 5):
            fibre.append(x)
    assert fibre == [5, 17]
    return {'schema': 'adva.crt-source-boundary.calibration', 'version': 0,
            'status': 'FiniteCounterexampleChecked', 'instances': records,
            'noncoprime_diagnostic': {'moduli': [4, 6], 'domain': '[0,24)',
                                     'observation': [1, 5], 'fibre': fibre, 'lcm': 12},
            'enumerated_nodes': nodes, 'node_limit': 256, 'timeout_seconds': 5,
            'wall_ms_before_report': (time.perf_counter() - start) * 1000,
            'process_peak_rss_kib_linux': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform == 'linux' else None,
            'native_calls': 0, 'new_native_vocabulary': 0,
            'unmeasured': ['research and authoring', 'retrieval', 'report serialization'],
            'residual': 'No Adva source-to-projection witness or equivalence between checker independence and coprimality is constructed'}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
