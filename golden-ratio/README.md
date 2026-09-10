# Golden-ratio resources: staged inputs, not admitted results

Status: staged external resources with one executed bounded calibration,
2026-09-10. Direction: Mingli Yuan / 苑明理. Formalization and bounded
execution: assistant.

This directory stages every artifact delivered in the local golden-ratio
resource directory, byte for byte and under canonical names. It is an input
home, not a result home: staging grants no native admission, no stable
keyword, no proof authority and no geometric reading.

- `index.json`: the single resource index. It records each artifact's
  delivered name, staged path, role, SHA256, byte count, digest source and
  the check that consumes it.
- `atlas/golden_ratio_atlas.md`: the delivered atlas. It is a human research
  presentation with derivations, corrections and an explicit next step. Its
  prose is quoted, never validated for truth.
- `source/`: the delivery container and its members: the external exact
  checker, its recorded output, the illustrative rendering source and image,
  and the delivery digest record.
- `source/reference/Golden_ratio.pdf`: the captured source object.
- `plates/`: seven illustrative plates.

## Why the plates and the PDF are not evidence

A figure is not a certificate. The plates are documentary illustrations whose
dimensions and digests are checked and whose *content* is not; no incidence,
length, angle or proportion is read out of a rendered picture here. The PDF is
a browser print-to-PDF capture; the bounded calibration confirms only that it
is a well-formed PDF whose metadata and whose cited revision identifier agree
with the atlas. Neither the PDF nor a plate may be cited as a witness for any
arithmetic or geometric claim.

## The delivered digest record is incomplete

`source/SHA256.json` covers five container members. The seven plates and the
PDF carry no delivered digest. Their pins are therefore first established at
staging time and are internally consistent only: a digest recorded here cannot
prove that a delivered plate is what its author intended to deliver. The
container's atlas member *is* byte-identical to the loose delivered atlas, and
that equality is checked.

## Bounded replay

The resource set is consumed by
[`experiments/golden_ratio/calibration.py`](../../experiments/golden_ratio/calibration.py),
under the frozen contract in the same directory:

```sh
python3 -S experiments/golden_ratio/calibration.py --output target/golden-ratio-fresh.json
```

The run verifies every staged artifact against `index.json`, compares the
container against the staged members and the delivered digest record, replays
the delivered external checker in a bounded child process and compares its
output with the recorded one, and then performs its own exact checks: the
quadratic field, the Fibonacci and bracket identities, the affine word and its
controls, rectangle coverage and residual, icosahedral incidence, the eight
source corrections as refusals, and a separation of four receipt kinds. The
output file must not already exist. The retained witness is
[`experiments/golden_ratio/evidence.json`](../../experiments/golden_ratio/evidence.json),
and
[`tests/python/test_golden_ratio_calibration.py`](../../tests/python/test_golden_ratio_calibration.py)
re-runs the calibration, compares it with that witness, and checks that a
tampered artifact, a tampered container record, a missing receipt contract and
an existing output path are each refused.

## What the figures may be used for

Nothing here reads a plate. The delivered images carry no metadata, no scale and
no caption, and the atlas names none of them, so every content gloss in
`index.json` is marked name-derived. The proposed figure-to-claim
correspondence, with what the bounded run did and did not establish for each
figure, is [section 3 of the research record](../../docs/research/golden-ratio-receipts-and-source-boundaries.md).

## Boundary

Staging and replaying these resources does not make the golden ratio part of
the Adva kernel, the Lisp surface, the IR or the stable API. It creates no
native word, no typed field extension, no `Seal`, and no successor in the
Pascal-rooted geometry growth line; the math catalog records the material as an
external reference whose obligation stays Open. The Python witnesses here are
external oracles under the authority rule in `AGENTS.md`.

See [the research record](../../docs/research/golden-ratio-receipts-and-source-boundaries.md),
the [receipt terminology contract](../../docs/terminology/golden-ratio-receipt-v0.json),
and the catalog entries `arithmetic-golden-ratio-receipt-calibration` and
`geometry-golden-ratio-external-reference`.
