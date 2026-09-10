# A disclosed-source projection witness

Proposed external research checker, 2026-09-10. Direction: Mingli Yuan;
formalization and execution: ChatGPT. Follows the CRT source-boundary
counterexample at library PR #3 commit `01cf5851474792773d1e9bf210895c53f4dbd8b4`.

## Frozen question and scope

Can the receiver independently verify that two reported residues came from
one previously fixed, disclosed integer record under one fixed projection
policy? Source and policy hashes are supplied by the caller, separately from
the witness. A witness cannot replace these expected pins with its own choice.

Source grammar: a JSON object with `schema`, `record_label`, `value`.
Policy grammar: a JSON object with `schema`, two ordered `moduli`, and the
interval `[0,m*n)`. Witness grammar: source/policy SHA-256 and two ordered
division rows. Each row has slot, modulus, quotient, remainder. Version-zero
schemas and exact object fields are checked. All numbers are exact integers,
with booleans excluded. The source lies in `[0,1024]`, moduli in `[2,32]`,
and quotients in `[0,1024]`. Every input file/string is at most 4096 bytes;
JSON duplicate keys are rejected. This is a finite disclosed-source baseline,
not a private witness, an unknown-source solver, or a native SourceId.

One route, two source instances `(3,4,5)` and `(5,7,17)`, at most 32 checks
and five seconds for the run. No theorem search, native call or external
artifact execution. Coverage absence returns Unknown; malformed, mismatched
or false claims return Rejected. A successful check is narrowly named
`RecordedSourceProjectionChecked`.

The generator uses `divmod`. The checker independently verifies, for each
ordered row, `value = quotient * modulus + remainder` and
`0 <= remainder < modulus`. The checker performs no modular inversion, CRT
reconstruction or implicit coprimality assumption. This is compatible with
keeping invertibility as a separate obligation. There is no floating point,
noncommutative rewrite, zero division, arithmetic-domain conversion or
contraction of equal-valued source occurrences.

## Trust and refusal boundary

The positive result has three explicit conditions: exact source bytes matched
the caller's pin; exact policy bytes matched the caller's pin; every declared
observation row has a checked division equation. All three are needed for this
particular status. No native free, Seal or semantic identity follows.

Controls include a false remainder, false quotient, noncanonical remainder
with an otherwise equal division equation, missing/duplicated/reordered rows,
replacing both the source and its self-consistent witness, replacing both the
policy and witness, an equal value in a different record, an out-of-domain
alias with the same residues, missing source, and a boolean source value.
The caller's fixed pins are retained for substitution controls. The alias and
boolean controls intentionally supply matching pins so the domain/type gates
are tested independently of hashing. Missing source or a missing row stays
Unknown; it is not false mathematics or evidence of a complete observation.

The caller must obtain its expected pins through a separately justified
boundary. Accepting a newly supplied pin merely because it accompanies a
witness would reopen the prior substitution problem. Hashes establish byte
integrity relative to that choice, not authenticity, truthful measurement or
social trust. `record_label` distinguishes exact documentary records here;
it does not create a Rust semantic identity. Even a valid receipt for source 5
does not prove that a physical measurement really was 5.

Because the value is disclosed, a receiver could directly compute its residues.
This certificate makes the claim and its checks explicit and serializable;
it claims no acceleration, secrecy, new expressiveness or universal grammar
completeness. It is not yet the native Adva source-to-projection witness.

## Replay and continuation

From the library root:

```sh
timeout 5s python3 calibrations/source-projection-witness-v0/calibrate.py
```

The finite checker is `projection.py`; `check` takes exact source, policy and
witness byte strings plus the two independent expected digests. `None` denotes
unavailable input. The calibration report retains every positive input byte
string, expected pins, witness, judgment, changed-input controls and costs.
The second source instance reuses the same builder and checker. JSON report
round-trip replay is separately recorded and charged. No fixture is promoted
to a theorem about all bounded inputs.

This helps a person or agent reject a consistent-looking observation obtained
from the wrong record while preserving missing coverage as Unknown. Usefulness
for Jiamin's task remains unmeasured. Next: choose a real repository record and
the pre-existing caller-side authority for its expected pin, then adapt that
specific projection without inventing a native identity. The physical-source
and undisclosed-source cases remain open. The nine original symbol-surface
obligations and complete native archive Unknown status are unchanged.
