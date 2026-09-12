# A typed entry word Start for the disclosed-source projection

Proposed external research calibration, 2026-09-12. Direction: Mingli Yuan;
formalization and execution: deepseek-v4-pro (DeepSeek Harness), submitted
through the author's account as an authorized proxy; he has not reviewed or
endorsed it, and his name is not evidence for any content here.

## What the word is

`Start` is the typed entry word of a disclosed-source residue projection:

```
Start : DisclosedIntegerRecord x ResidueProjectionPolicy -> OrderedResiduePair
```

- **Domain ports** (ordered): `source`, `policy` — the same disclosed record
  and projection-policy schemas used by `source-projection-witness-v0`.
- **Codomain ports** (ordered): `r0`, `r1` — the two remainders bound to the
  policy moduli in slot order.
- **Body**: one `divmod` per policy modulus. No CRT reconstruction, no modular
  inverse, no floating point, no contraction of equal-valued occurrences.

## The judgment: the three conditions, unchanged

The positive judgment `StartWordChecked` presents **exactly** the three
conditions of the source-projection witness, inherited verbatim:

1. **C1 (source pin)**: the exact source bytes match the caller's independent
   `expected_source_sha256`, and the witness's own `source_sha256` agrees.
2. **C2 (policy pin)**: the exact policy bytes match the caller's independent
   `expected_policy_sha256`, and the witness's own `policy_sha256` agrees.
3. **C3 (division equations)**: every declared observation row satisfies
   `value == quotient * modulus + remainder` with `0 <= remainder < modulus`,
   the row modulus equals the policy modulus of its slot, slots are distinct
   and ordered (this is the slot-to-port binding), and both ports are covered.

The word layer adds only the typed reading: the same judgment is read through
the declared domain/codomain frontier, and the ordered residues are returned
as the port values `(r0, r1)`.  Every other gate is a refusal or an Unknown,
unchanged from `source-projection-witness-v0/projection.py`: schema and field
gates, the integer domains `[0,1024]` for the source value and `[2,32]` for
moduli, the interval `[0, m*n)`, byte budgets, and duplicate-JSON-key
rejection.  Missing input or fewer than two covered rows returns `Unknown`;
a failed gate returns `Rejected` with its reason.

## Boundary of claims

- This calibration reuses the two positive instances `(m,n,x)=(3,4,5)` and
  `(5,7,17)` and the twelve mutation controls of the source-projection
  witness, so the two judgments can be compared gate by gate.
- A green run is a statement about verification, not progress.  `Start` creates
  no native operation, no native type, no Rust authority, and no `Seal`.
- `physical_source_truth` stays `NotEstablished`; the caller must obtain its
  expected pins through a separately justified boundary.

## Replay

From the library root:

```sh
timeout 5s python3 calibrations/start-word-v0/calibrate.py > \
  calibrations/start-word-v0/report.json
```

The finite checker is `start_word.py`; `calibrate.py` runs the bounded
calibration and writes the report.  Budget: at most 32 checks and five seconds.
The report retains every positive input byte string, expected pins, witness,
typed judgment, changed-input controls and measured costs.
