# Adva library — the content and library layer

Status: a **separate repository** (`mountain/adva-library`), mounted as a git
submodule at `adva-library/` inside the main [`adva`](../README.md) repository.
It is **documentary only**. Nothing here is native admission, and no byte here
becomes a native operation, type or builtin by being catalogued.

Paths beginning `../` refer to that parent repository. This library is normally
read through it, and several of its checkers live there rather than here.

## What this is, and what it is not

- **It is** the durable home of delivered research inputs, presentations and
  content, together with the catalog that governs how each may be cited and
  reused. Two kinds of thing live here, and they are not the same:
  **delivered artifacts under byte pins**, and **catalog and admission metadata**
  that describes them.
- **It is not** a module system, a loader, a language runtime, a self-growing
  knowledge base, or a source of semantic authority. The main repository's Rust
  kernel is that authority, and it does not read this directory to decide what
  is true.
- **A digest records byte integrity only** — never authentication, semantic
  identity, or proof. Registering a document changes what may be *cited*; it does
  not change what is *true*.

## How to check it

The checker lives in the main repository, not here. Run it from that
repository's root:

```sh
python -S python/adva/adva.py math-check --key-words
```

It checks metadata, directory membership and pinned bytes, and reports the
growth obligation. Success grants **no** native admission and no proof authority.
It reads a bounded number of declared files under a declared entry budget, so a
new entry can require raising that budget explicitly rather than implicitly.

## The rules that govern this layer

- **One home per entry.** An entry has exactly one owning topic directory.
  Appearing elsewhere is a reference, not a second home.
- **A cross-topic reference is a documentary view.** It is never a derivation
  parent, an implicit import, or a permission transfer.
- **A documentary `seal` is not a Rust `Seal`.** The growth obligation's seal
  pins an obligation; it does not discharge it.
- **The geometry growth obligation is `Open`, and its native `Seal` is
  `NotIssued`.** Geometry successors need a proposed same-directory ancestry
  reaching the pinned Pascal root and, before admission, native import and
  derivation certificates that do not yet exist.
- **A recorded status names what the bytes are, not what they prove.** A note
  that ships a checker is an external calibration record; a delivered
  presentation is a proposed document; neither is native admission.
- **A name is not an admission.** Cataloguing, renaming, or registering a
  document does not register an operation, and it does not bridge two tasks by
  making them share a word.

## What is here

| Area | Holds | Recorded as |
|---|---|---|
| `index.json`, `pascal-task.adva`, `pascal-witness.adva` | the delivered Pascal task and witness pair | proposed research documents |
| `learn-free-six.contract.json`, `phase-runner/` | the six-slot orchestration contract and its pinned inputs | orchestration contract |
| `math/` | one strict manifest, three topic indexes (arithmetic, geometry, logic), and the growth obligation | documentary catalog |
| `stability/` | Rust-checked research library epochs 0000 and 0001 | checked research snapshots |
| `exploration/0151/` | proposal recipes and their journal | replayable proposal journal |
| `calibrations/` | bounded external calibrations with reports | external calibration records |
| `golden-ratio/` | a staged resource set: atlas, plates, source and reproducer | staged delivery |
| `names/` | the party naming layer and the catalog key words | proposed documents |
| `symbol-surface/` | name-to-record swap, receipts, and a bounded text transport | proposed with open obligations |
| `prime-universe/`, `knowledge-boundary/` | proposed finite tasks and distinction examples | proposed documents |
| `meaning-*.md` | proposed duality documents, each with one topic home | proposed documents |
| `validation/` | install-and-run acceptance records | acceptance records |
| `vendor/` | pinned third-party submodules, not audited here | external dependencies |

Every entry in `math/manifest.json` carries its own scope, assumptions,
checker, evidence pins, open obligations and forbidden conflations. Read the
entry, not this table, before reusing anything.

---

## The delivered Pascal pair

- `pascal-task.adva`: three distinct Human/World/Machine roles, a shared Pascal
  question, finite resources, an explicit meeting gap and acceptance scope.
- `pascal-witness.adva`: three presentations, the normalized conic proof,
  exact arithmetic checks, reuse and counterexamples, and retained residuals.
- `index.json`: file types, byte digests, source attribution and native status.
- `learn-free-six.contract.json`: orchestration contract with three six-slot
  phases: `learn` (draft #136 roundtrip), `run` (bounded native program-run
  transport; output recorded as bytes, not interpreted) and `free` (adapter
  remains absent until its meaning is defined).
- `phase-runner/`: the fixed native learn method inputs copied from draft
  PR #136, pinned to commit `4cbbfebfead3918b4da46920d55708d10f3baee8`, plus
  `run-program.adva`, a byte copy of `programs/native-run/arithmetic.adva`
  serving as the run phase's pinned subject.

The Pascal files are preserved byte for byte from their delivered versions.
They remain proposed research JSON documents. Their arithmetic is external
evidence, not a native Rust import certificate. The three Human identities,
meeting time/place and acceptance are unresolved. Placing them in this
directory does not register `run`, `free`, an interpreter, or a builtin.

The six-stage roundtrip does not execute the Pascal documents. It is a
separate existing arithmetic calibration useful for testing orchestration.
The missing Pascal importer must remain visible; this directory does not
bridge the two tasks by renaming files.

### The bounded runner

From the repository root, use a new report directory:

```sh
python experiments/phase_runner/run_six.py \
  --contract adva-library/learn-free-six.contract.json \
  --report-dir target/learn-free-six
```

With no backend supplied, this records the missing implementation and zero
native launches. It produces `learn-report.json`, `run-phase-report.json`,
`free-report.json` and the overall `run-report.json`. Six report slots are not
six executions or six successes.

The existing learn calibration can be invoked after obtaining an executable
built from the declared draft source:

```sh
python experiments/phase_runner/run_six.py \
  --contract adva-library/learn-free-six.contract.json \
  --report-dir target/learn-free-six-with-backend \
  --backend /absolute/path/to/adva
```

The command hashes the supplied binary for the record; a digest alone is not
authenticated build provenance. Supplying main's binary does not add #136's
draft method. The `free` phase remains blocked even when learn and run
succeed.
There is no Python substitute for the native arithmetic operation.

### Reporting and continuation

Each phase has six requested slots and an independent count of actual
launches. A missing adapter records NotRun. A timeout preserves Unknown; a
guard refusal, invalid output or backend error stops that phase and preserves
the remaining slots as NotRun. Partial output files are retained. Inputs and
outputs are hashed for integrity, without assigning native semantic identities.

A Completed slot means that the configured subprocess protocol completed.
It is not a universal learning theorem, a proof of free, human acceptance,
or an independent semantic validation by Python. The native backend remains
responsible for arithmetic and history validation. Fatal report-storage
failure can still occur and must be surfaced; no program promises that all
physical execution and I/O errors are impossible.

Child cleanup is limited to the process group created for each backend call.
This supervisor is for a declared backend; it is not a security sandbox for
programs that deliberately detach or evade operating-system limits.

See `docs/research/0139-library-six-phase-and-communication.md` for the missing
free predicate and the distinction among contract, seal and Seal.

### Checked research library epochs (Research 0150)

`stability/epoch-0000.json` and `stability/epoch-0001.json`, when published by
the bounded 0150 run, use a **separate Rust-checked snapshot format**. They do
not change the documentary status of the Pascal files or `index.json`.
The loader `adva_witness::load_library_v0(directory, epoch, budget)` rechecks
the full bounded parent chain and reconstructs native research witness nodes.
It does not trust decoding, stored status flags or digests alone.

The `library_epoch` Cargo example bootstraps from the retained 0149 proposal,
loads that published snapshot, performs one supplied candidate/observation
update, publishes the next epoch and reloads its guarded witness. An explicit
new directory and report path are required; existing snapshots are never
overwritten. See [the finite contract](../docs/research/0150-persistent-library-epochs.md)
and its separate execution evidence. This remains a research loader, not a
stable Lisp module system or automatically self-growing knowledge base.

### Proposal exploration journal (Research 0151)

The `library_generation` example reads the checked `stability/` seed and
generates exact arithmetic candidates from it. Successful compositions are
retained as proposal recipes under `exploration/0151/`, not published as a new
knowledge epoch. The example replays the complete journal before using a
recipe in a later bounded search; decoding alone never authorizes reuse.
Rejected candidates, expanded alternatives, nonzero checks and macro/disabled
controls remain visible. See the [finite contract](../docs/research/0151-library-driven-proposal-feedback.md).

### External arithmetic calibration (Research 0152)

The outer `python/adva/adva.py verifier-search` command loads the unchanged
`stability/` seed through Rust, then checks selected arithmetic rewrite steps
with Rust witnesses, Lean proofs and Metamath proofs. Its separate evidence
and path journal live under
[`docs/research/0152-evidence/`](../docs/research/0152-evidence/README.md).
The comparison can change a research search policy, not the old library's
meaning. There is no new knowledge epoch, new native word, silent deletion of
backtracking paths, or promotion of external equality to program identity.

Research 0153 keeps these epochs and recipe journals fixed during a policy
comparison and conditional 100-round campaign, invoked through
`python/adva/adva.py search-campaign`. Its separate
[campaign evidence](../docs/research/0153-evidence/README.md) retains the
selected proposal policies, complete traversals and checked batch receipts.
A selected policy is not a new library word, and no epoch is published by
completing a round.

### The constrained math topic view

[`math/`](math/README.md) now indexes existing arithmetic, geometry and logic
materials through one strict manifest and three topic indexes. Each entry has
one home; other topics may hold documentary references, not derivation rights.
Existing snapshots, journals, the Pascal pair and this directory's original
`index.json` are not moved or reinterpreted. `adva.py math-check` checks only
metadata, directory membership and pinned bytes; success grants no native
admission or proof authority.

The version-zero growth obligation is fixed by a documentary `seal`, with
status Open and native Seal NotIssued. Geometry successors need a proposed
same-directory ancestry reaching the pinned Pascal root and, before actual
admission, the still-missing native import and derivation certificates.
Unconnected braid material stays external reference. Existing external Pascal
calculation and finite logic experiments are indexed, but not promoted to a
native task-loop API. See ADR 0042 and Research 0154 for the precise boundary.

The detailed Chinese note
[密码学封存、双语言校准与 Adva 的信任边界](../docs/research/0155-cryptographic-sealing-and-calibration-boundary.md)
is registered as a proposed logic-home document, with an arithmetic reference.
It compares Python/Rust support for Ed25519, AES-256-GCM and
ChaCha20-Poly1305, separates signatures from native proofs, and records the
key-management, directory and finite-run obligations for any later work.
This registration installs no crypto dependency, issues no signature or
native Seal, and starts no calibration run.

### The symbol surface swap proposal

[Symbol surface swap v0](meaning-symbol-surface-swap-v0.md) is the library-side
companion to Adva PR #170: a name-to-record view with unchanged source bytes,
explicit provenance, finite structural checks and nine open obligations.
It introduces no native swap or automatic execution.

The [native-load receiving acknowledgment](symbol-surface/receipts/native-load-v0/README.md)
binds the subsequent peer reply and scoped text audit to that historical handoff.
Peer execution, receiver validation and the incomplete archive remain separate;
all nine obligations stay Open.

A [bounded text transport tool](symbol-surface/transport-v0/README.md) now provides
the producer and receiver commands for the missing artifact. Two synthetic
transfers are checked; the real native artifact remains NotReceived here.
