# Receive the native-load reply without widening its guarantee

Status: Proposed documentary acknowledgment, 2026-09-10.

The library's original `handoff.json` asked whether the Rust loader could read
the retained envelope while leaving all nine annotations open. Adva main at
`e0e3433ebcaa2da6ec3e0bc1f67bd316f2c38547` now contains a peer-reported
native run. This receipt binds that reply to the original library handoff and
to the narrower text audit in Adva PR #172 at
`feef303c35ab2d10e3f7763cb0bd73e216e0571e`. The audit is an unmerged proposal;
its location is intentionally distinct from the peer's merged result.

## Frozen question and budget

Can this receiver bind these three exact JSON records to the historical
handoff without losing an obligation or promoting a partial audit to a full
verification? Objects are pinned UTF-8 bytes and finite JSON records. The
quantifier is over these three records and the nine retained annotation
entries only. No arithmetic domain, game, theorem search, new native grammar
or mathematical evaluation is introduced. Comparisons are byte hashes,
strings, bounded nonnegative counts and ordered JSON structures.

One route, zero search candidates and zero native calls. Six input files,
at most 65,536 bytes each, four relation controls and a five-second process
timeout. Checking the saved receipt reads one additional bounded file.
No retries, polling or fuel renewal. A changed upstream record requires a
separate versioned comparison; it must not be silently repinned in v0.

## Inputs, output and judgment boundary

`sources.json` records exact repository, commit, path, length and SHA-256 for
the three unchanged imported records. `receive.py` also freezes their hashes
and provenance independently of that manifest. These pins provide integrity
relative to the chosen commits, not author authentication or build security.

`receipt.json` is a deterministic documentary result. Its
`RecordedReplyBoundToHandoff` status describes the checked record relation;
it is not a native Adva judgment or a new language word.

| Boundary | Retained judgment |
| --- | --- |
| Peer native execution, as reported | NativeEnvelopeLoaded; ready; conditional |
| Previous receiver audit, as recorded | 53 text artifacts out of 54 archive artifacts checked |
| This receiver | Pinned records and their declared relation boundaries checked |
| Complete archive | Unknown; native gzip bytes unavailable to the previous text audit |
| Local native execution | NotRun |
| Mathematical discharges | 0; all nine original obligations Open |

The old handoff, its `NotObserved` field, eight source files and source
obligations remain byte-identical. They describe the earlier observation.
This new record describes receiving the later reply; it does not edit history.

## Replay and refusal controls

From the library root, using Python 3 and a shell with `timeout`:

```sh
timeout 5s python3 symbol-surface/receipts/native-load-v0/receive.py
```

This checks the saved receipt without rewriting it. `--write` constructs it
from the same frozen inputs. The checker rejects a wrong predecessor, a
missing/reordered obligation, a change of the audit's Unknown to Complete,
and an audit pointing to another source commit. Controls call the relation
checker directly after changing one field, so rejection is not merely the
earlier hash check noticing different bytes. A separately deserialized copy
must reproduce the same output; that is serialization replay, not a new
mathematical instance or a demonstration of learning.

`check-report.json` preserves the construction run's controls and costs.
Its time and RSS are local measurements; imported reports retain their own
cost accounts. They must not be added and presented as one native run.
Receipt serialization is measured separately; authoring, retrieval and
report serialization are unmeasured. No speedup or new expressiveness is claimed.

In a complete outer Adva checkout, overlay this library revision and run:

```sh
python3 python/adva/adva.py math-check --key-words
```

The existing `logic-symbol-surface-swap` entry indexes this acknowledgment.
The catalog remains at 17 entries, with no extra topic home or derivation right.

## Residual and next smallest step

The receipt does not replay the previous 53-file audit, inspect the binary,
authenticate the build, resolve payloads, discharge mathematics, or grant
native `free`. It helps a subsequent person or agent locate which side
asserted which result without asking Mingli to manually relay that context.
Usefulness for Jiamin's real task remains unmeasured.

Next, retain a bounded, lossless textual transfer of the pinned native gzip
artifact and independently check its decoded byte hash and archive inventory.
Only after that separate check may the complete-archive judgment change.
Even a complete archive would still leave local native replay and the nine
mathematical/representation obligations separate. No transfer or execution
is automatically triggered by this receipt.

Links: [peer result](https://github.com/mountain/adva/commit/e0e3433ebcaa2da6ec3e0bc1f67bd316f2c38547),
[text audit and native regression proposal](https://github.com/mountain/adva/pull/172).
