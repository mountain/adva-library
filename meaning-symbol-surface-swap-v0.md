# Symbol surface swap v0: ask from the name side

Status: **proposed-document / proposed-mapping**. Direction and vocabulary:
Mingli Yuan. Representation and bounded checks: ChatGPT.
Catalog home: `logic`; key: `logic-symbol-surface-swap`.

## The direction change

Adva [PR #170](https://github.com/mountain/adva/pull/170), frozen at
`6538f98555db89f0569aed39952d355bc10c0cd0`, starts from constructions and
records their proposed symbolic results. This library companion starts from
a symbol and asks which retained record, convention and missing witness can
support it. The source draft has not been merged at capture time.

Let a documentary row be `(record, name; metadata)`. This proposal defines
`swap(record, name; metadata) = (name, record; metadata)`. Applying it twice
restores that row. The third component retains origin, type, branch context,
occurrence history and open obligations through pinned source references.
The history of making the two views is not erased by this round trip.

This is an explicitly scoped **documentary endpoint swap v0**. Research 0160
uses `swap` for simultaneous matrix row/column basis permutations. We borrow
its discipline of retaining a permutation and its information boundary, not
its matrix operation or any native semantics. No stable word is redefined.
There is no Rust execution, complex conjugation, observer pullback `D*`,
semantic inverse, proof transport or new mathematical duality in this PR.

| Name-side question | Retained record | What remains missing |
| --- | --- | --- |
| What supports `i` here? | Its explicitly typed atom declaration | No construction witness for `i` was supplied in #170 |
| What supports `pi`? | The five-step `r-pi` equation journal | Native replay, nonzero denominators and branch justification |
| What supports `-1`? | The declared result of filling `H(a,b,c)=a-b*c` | Native typed translation and replay, preserving both occurrences of one |

All three rows remain `DeclaredNotExecuted`. A name is a question key, not
a proof or a unique recipe. The synthetic reuse control gives two different
records the same name and confirms that both survive the reverse view.
In general, the reverse of a relation is not an inverse function. Reordering
lost information cannot reconstruct it; retained source records are required.

## What crosses this boundary

All eight files of #170 are archived byte for byte under
[`symbol-surface/source/`](symbol-surface/source/). This includes the original
`.adva` envelope, external symbolic presentation, contract, nine open
obligations, scripts, report and explanatory note. Their historical statuses
and costs are not new library execution evidence.

The two new views are
[`record-to-name.json`](symbol-surface/record-to-name.json) and
[`name-to-record.json`](symbol-surface/name-to-record.json). They contain the
same relation rows with exchanged endpoint coordinates, plus a commit-pinned
source inventory and all nine open obligations. Their SHA-256 references
check documentary integrity, not authenticated authorship or native identity.
Source scripts are archived and are not run during the swap check.

The source's declared `S`, `S-bar` and `S-wedge` roles remain unchanged; no
numeric values are moved among them. The prefix codes `0`, `20`, `22` remain
addresses, not Cantor-set placements of `i`, `pi` and `-1`. Their finite-word
boundaries remain intact. No Cantor iteration or theorem application is run.
Schroeder-Bernstein, Knaster-Tarski and nested-interval applications remain
open. The game remains represented, with no allocated gameplay fuel.

The library entry has one logic home because it describes representation and
lookup. Its mathematical references do not become geometry derivation parents.
The Pascal root, original two-file index, existing epochs and fixed growth
obligation remain unchanged; native `Seal` is still NotIssued.

## Replay and review

From a standalone adva-library checkout on Linux:

```sh
timeout 5s python symbol-surface/swap.py
```

`--write` explicitly regenerates the two view files from the retained source;
the default command reads and compares them without rewriting them. A mismatch
fails. Bounds are eight source files, 64 KiB per input, at most sixteen relation
rows and a five-second external deadline. The script does not evaluate any
expression or execute any archived script. Its three controls cover the double
swap, a nonunique reverse lookup, and rejection of a `Proved` status promotion.
It is a finite documentary checker, not a general-purpose semantic validator.

The original outer Adva catalog checker must also pass against a checkout
with this library revision overlaid at `adva-library/`:

```sh
python python/adva/adva.py math-check --key-words
```

For that second check, use the outer source at
`17fe19e283011f3c4361112f2fe25e4cdae9407e`. The resulting catalog has seventeen
entries. A future outer gitlink update will also need to adjust tests that
explicitly assert the former sixteen-entry count; this library PR neither
updates that gitlink nor changes the outer checking rules.

This supports navigation from a question word back to its available support
and visible gaps. The strongest result is finite lossless reordering of the
retained documentary relation, not a theorem that a name determines its
meaning or that universal grammar is complete. Next: review this interpretation
of `swap`, then perform the source draft's missing read-only Rust load when a
compiler is available. No automatic proof run follows a successful lookup.

## PRs as the communication boundary

Mingli's follow-up identifies Observation and Measure as the work previously
mediated by his repeated linking between the two sides. The explicit
[`handoff.json`](symbol-surface/handoff.json) now records the source commit,
receiving branch, observation projection, finite measurements, residuals and
the next minimal question. Both PR descriptions link to their companion.
Authorized agents can read that record directly instead of requiring him to
copy the payload between conversations.

This turn observes eight preserved files, three swapped relation rows and
nine obligations before and after, with zero discharges. A later reply must
pin its predecessor, state what it observed and measured, retain unresolved
obligations and declare a finite exit. Unchanged evidence is EvidenceStutter,
not a reason to create repeated PRs. Source changes require a new comparison;
they never silently rewrite this checkpoint.

The PR is the transport and review surface. No background polling, webhook,
automatic reciprocal runner or peer acknowledgment is implemented or observed
here. Bidirectional links do not by themselves prove that the other agent
has read, accepted or acted on this handoff.
