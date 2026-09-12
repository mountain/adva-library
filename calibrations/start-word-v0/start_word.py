"""External finite typed entry word Start; no native semantic authority.

Start : DisclosedIntegerRecord x ResidueProjectionPolicy -> OrderedResiduePair

The positive judgment `StartWordChecked` presents exactly the three conditions
of the source-projection witness (calibrations/source-projection-witness-v0):

  C1  exact source bytes match the caller's independent pin,
  C2  exact policy bytes match the caller's independent pin,
  C3  every declared observation row has a checked division equation
      (value == quotient*modulus + remainder, 0 <= remainder < modulus),
      with slots bound to the ordered output ports (r0, r1) and full coverage.

The word layer adds only the typed reading: the two domain ports are
(source, policy) and the two codomain ports are (r0, r1) in slot order.  Every
other gate is a refusal or an Unknown, inherited unchanged from
source-projection-witness-v0/projection.py.  No CRT reconstruction, modular
inverse, floating point, native operation, type, or Seal is introduced here.
"""
import hashlib
import json


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':')).encode('utf-8')


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def unique(pairs):
    out = {}
    for key, value in pairs:
        require(key not in out, 'DuplicateJsonKey')
        out[key] = value
    return out


def parse(raw):
    require(type(raw) is bytes and len(raw) <= 4096, 'InputTypeOrBudget')
    return json.loads(raw, object_pairs_hook=unique)


def fields(obj, expected):
    require(type(obj) is dict and set(obj) == set(expected), 'ObjectFields')


def integer(x, lo, hi):
    return type(x) is int and lo <= x <= hi


def typed_boundary():
    """The fixed typed frontier of the word Start."""
    return {'domain_ports': ['source', 'policy'], 'codomain_ports': ['r0', 'r1']}


def build(source, policy):
    """Fixture constructor; acceptance always requires the separate check."""
    s, p = parse(source), parse(policy)
    rows = []
    for i, m in enumerate(p['moduli']):
        q, r = divmod(s['value'], m)
        rows.append(dict(slot=i, modulus=m, quotient=q, remainder=r))
    return encode(dict(schema='adva.record-projection-witness.v0',
                       source_sha256=digest(source), policy_sha256=digest(policy), rows=rows))


def check(source, policy, witness, expected_source_sha256, expected_policy_sha256):
    if source is None or policy is None or witness is None:
        return {'status': 'Unknown', 'reason': 'InputUnavailable'}
    try:
        require(type(source) is bytes and type(policy) is bytes and type(witness) is bytes
                and max(len(source), len(policy), len(witness)) <= 4096, 'InputTypeOrBudget')
        require(digest(source) == expected_source_sha256, 'SourcePinMismatch')
        require(digest(policy) == expected_policy_sha256, 'PolicyPinMismatch')
        s, p, w = parse(source), parse(policy), parse(witness)
        fields(s, ['schema', 'record_label', 'value'])
        fields(p, ['schema', 'moduli', 'interval'])
        fields(w, ['schema', 'source_sha256', 'policy_sha256', 'rows'])
        require(s['schema'] == 'adva.disclosed-integer-record.v0' and
                p['schema'] == 'adva.residue-projection-policy.v0' and
                w['schema'] == 'adva.record-projection-witness.v0', 'Schema')
        require(type(s['record_label']) is str and 1 <= len(s['record_label']) <= 64, 'RecordLabel')
        require(integer(s['value'], 0, 1024), 'SourceInteger')
        require(type(p['moduli']) is list and len(p['moduli']) == 2 and
                all(integer(m, 2, 32) for m in p['moduli']), 'Moduli')
        require(type(p['interval']) is list and len(p['interval']) == 2 and
                all(type(x) is int for x in p['interval']) and
                p['interval'] == [0, p['moduli'][0] * p['moduli'][1]], 'Interval')
        require(0 <= s['value'] < p['interval'][1], 'SourceOutsideDomain')
        require(w['source_sha256'] == expected_source_sha256 and
                w['policy_sha256'] == expected_policy_sha256, 'WitnessPinMismatch')
        require(type(w['rows']) is list and len(w['rows']) <= 2, 'RowBudget')
        slots = []
        for row in w['rows']:
            fields(row, ['slot', 'modulus', 'quotient', 'remainder'])
            require(integer(row['slot'], 0, 1), 'Slot')
            slots.append(row['slot'])
        require(len(set(slots)) == len(slots), 'DuplicateSlot')
        require(slots == sorted(slots), 'RowOrder')
        for row in w['rows']:
            m = p['moduli'][row['slot']]
            require(type(row['modulus']) is int and row['modulus'] == m, 'RowModulus')
            require(integer(row['quotient'], 0, 1024) and
                    integer(row['remainder'], 0, m - 1), 'DivisionRange')
            require(s['value'] == row['quotient'] * m + row['remainder'], 'DivisionEquation')
        if len(w['rows']) < 2:
            return {'status': 'Unknown', 'reason': 'ObservationCoverage', 'checked_rows': len(w['rows'])}
        return {'status': 'StartWordChecked',
                'typed_boundary': typed_boundary(),
                'ports': [row['remainder'] for row in w['rows']],
                'source_sha256': expected_source_sha256, 'policy_sha256': expected_policy_sha256,
                'observations': [row['remainder'] for row in w['rows']],
                'checked_rows': 2, 'physical_source_truth': 'NotEstablished', 'native_admission': 'NotGranted'}
    except (ValueError, TypeError, KeyError, UnicodeError, RecursionError) as error:
        return {'status': 'Rejected', 'reason': str(error)}
