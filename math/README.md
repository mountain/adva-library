# Math: a constrained documentary topic view

This directory implements Mingli Yuan's proposal to place **arithmetic,
geometry and logic** under `math/`. Logic's proposed **降位** is recorded as
an organizational change: inference systems can be research content with
assumptions and evidence. A directory does not implement semantic lowering,
change the rules checking that content, or settle a historical classification
of logic. See [ADR 0042](../../docs/adr/0042-math-topic-catalog-without-semantic-authority.md).

## Two independent coordinates

- **Topic**: arithmetic, geometry, logic. An entry may appear in several views.
- **Recorded evidence state**: hypothesis, proposed document, checked research
  snapshot, proposal journal, bounded evidence, external calibration, policy
  evidence or checking-boundary description.

Neither coordinate is a native type, semantic identity, permission to execute,
or a new knowledge epoch. Topics are not assigned to compute/verify/learn or
Rust/Lean/Metamath. The tree is not a theorem about knowledge-space topology.

`manifest.json` records each documentary entry once, including its theory and
version, assumptions, scope, material/evidence references, original checker
description, reuse requirements and unresolved obligations. Three
`<topic>/index.json` files contain keys into that manifest, partitioned into
`owned` and `references`. Every entry has one `home`; new keys require its
topic prefix. Shared topic membership never grants local ownership, imports
programs, identifies two programs or copies their evidence.

## Current contents

| Topic | Memberships | Examples |
| --- | ---: | --- |
| arithmetic | 8 | epochs 0/1, recipes, three-verifier calibration, 100-round evidence, Pascal presentation, crypto calibration reference, golden-ratio receipt calibration, period-three matrix calibration |
| geometry | 5 | Pascal root, external Q4/M6 reference, proposed Pascal incidence-task successor, golden-ratio external reference |
| logic | 16 | fixed rules, finite logic tasks, cryptographic boundary, naming and interpretation proposals, the Nim rule-constraint typing |

There are **25 distinct entries**, with 29 topic memberships. Counts are
recomputed from the manifest rather than carried over from an earlier
revision, and they describe this catalog only, not an inventory of all project
knowledge. The column is headed memberships because each row counts topic
memberships, not entries: one entry may appear in several views. An earlier
revision of this table read 23 entries and 27 memberships because it had been
written before the period-three matrix calibration was appended; that stale
count is corrected here rather than left to drift. In particular, Pascal remains proposed; M6 retains its missing
filler; logic has no newly installed native calculus. The old
`adva-library/index.json` remains its original two-document catalog.

[Research 0155: 密码学封存、双语言校准与信任边界](../../docs/research/0155-cryptographic-sealing-and-calibration-boundary.md)
adds a proposed document about SHA-256/BLAKE3 digests, Ed25519 signatures,
AES-256-GCM/ChaCha20-Poly1305 interoperability, independent trust roots and
bounded external calibration. Its single home is logic; arithmetic only
references the finite-computation discussion. This is not a classification of
all cryptography as logic. It adds no geometry entry, proof, installed crypto
dependency, signed obligation or executable task. The proposal has no checker
or execution evidence and does not change the Open growth obligation.

[ADR 0043: 目录分割工程合同](../../docs/adr/0043-directory-partition-contract.md)
把 adva-library 的目录角色、跨目录规则、准入程序与修订纪律收拢为一份
proposed 合同（JSON 同目录），并登记为本目录学条目（logic，
`logic-directory-partition-contract`）。它不改变检查器、增长义务或任何
已 pin 字节；math-check 通过仍只允许浏览声明引用。

[Party naming layer](../../docs/research/../adva-library/names/party-naming-layer-v0.json)（条目
`logic-party-naming-layer`）：按明理 2026-09-09 裁定执行方案 A——
Machine→Substrate（基底）、World→Knowledge（知识）、Human→Surface（界面）。
pascal 原始字节不动，只新增文档映射；不声称三机识别。

[意义解读 v0](../../docs/../adva-library/meaning-interpretation-v0.md)（条目
`logic-meaning-interpretation`）：机制与解读互为对偶的两张 H²，由第三个
对象（dual-pair-receipt）标记；6 维泰西穆勒与 Calabi-Yau 读法记为假设。
散文不被验证为真。

[Yau-Calabi 映射 v0](../../docs/../adva-library/meaning-yau-calabi-mapping-v0.md)（条目
`logic-yau-calabi-mapping`）：丘先生 Calabi 历程的五锚点算术映射 +
对偶谱支柱；proposed-mapping，待人类评审；非等同声称。

## Read-only check through the outer CLI

From the repository checkout, using Python's standard library on POSIX:

```sh
python3 python/adva/adva.py math-check
```

For an optional fresh report (the parent directory must already exist):

```sh
python3 python/adva/adva.py math-check --output target/math-catalog-check.json
```

`--root /path/to/adva` chooses another checkout. The catalog location within
that root is fixed; entries cannot replace its policy or choose another
directory as a logic authority. This command requires neither the PyO3
extension nor Rust builds, Lean, Metamath, network access or search.

The checker checks strict schemas, explicit fields, topic coverage and SHA256
reference integrity. It refuses duplicate keys, unsupported status/permission
fields, changed policy, noncanonical/escaping paths, symbolic links and
nonregular referenced files. It reads only the declared catalogs and
references; an unlisted file cannot register itself by sitting in a folder.
Evidence is hashed, **not parsed or verified**. Consistent pins are not
authentication, and recorded statuses and prose are not validated for truth.

| Report status | Meaning | CLI exit |
| --- | --- | ---: |
| `CatalogConsistent` | Documentary shape, membership and referenced bytes match | 0 |
| `InvalidCatalog` | A checked constraint or file read failed | 2 |
| `Unknown` | A declared resource bound prevented completion | 3 |

Every report has `native_admission: not-granted`, `proofs_rechecked: false`,
and `recorded_claims_authenticated: false`. Success permits only browsing
declared references. Real reuse still needs the original Rust/prover checks
and their own contracts. The checker does not decide that a recorded theorem,
assumption, theory translation or checker is correct.

## Operational boundary

The fixed [growth obligation](constraints/growth-obligation-v0000.json) is
retained with a [documentary seal](constraints/growth-obligation-seal-v0000.json).
It records `Open` / native `Seal` **NotIssued**, not a discharged proof. Both
the checkpoint and the exact obligation pin are checked; there is no automatic
resealing command. The original root is `pascal-research-presentations` and
must retain the exact original Pascal documents.

Geometry candidates must cite earlier same-home parents reaching that root.
An external reference, cross-home parent, alternative root, missing or cyclic
parent chain, or asserted native discharge is refused. A candidate may retain
external derivation evidence, but no such reference is sufficient for native
admission. Q4/M6 remains an external reference. The existing Research 0128
Pascal task is a proposed successor with native import/transport still Open.
The checker admits **zero native geometry successors**.

These are catalog/CI gates and agent obligations, not an OS sandbox or a new
program publication mechanism. Existing geometric or logical routines outside
this catalog keep their original research scope. See the
[task-loop audit](../../docs/research/0154-math-catalog-and-task-loop-boundary.md)
for what they can already compute.

Bounds are 32 entries, 256 reference occurrences, 96 files, 256 KiB per
metadata file, 8 MiB per referenced file, 32 MiB total read bytes and a
five-second cooperative deadline between reads. No subprocesses, retries,
recursive imports, proof replay or pin repair are performed. This is a local
quiescent-checkout check, not an atomic repository snapshot or an OS watchdog
against blocking filesystem I/O. A fingerprint change requires a reviewed
catalog edit; the checker never updates a digest for the user.

Existing materials remain at their original locations. No epoch, recipe,
proof source, path log or verifier rule is moved or rewritten. The additive
CLI change gives `adva.py` a new hash: Research 0153's historical pins remain
unchanged and refer to its original runtime commit `5d956de` (merge `8c94621`).
Use that revision for the historical campaign; this catalog does not rerun it.

## Revision discipline

Add documentary keys explicitly, declare every applicable topic, and preserve
the distinction between an asserted evidence state and actual proof admission.
Keep cross-domain interpretation obligations visible. A new topic or schema
requires an explicit catalog version/design decision, not a reinterpretation
of v0. Studying a candidate logic never authorizes changing the frozen checker
inside a running experiment. Semantic promotion remains subject to the
existing research agenda and Rust authority boundary.

## Golden-ratio resources as an external reference

[Staged golden-ratio resources](../golden-ratio/README.md) are registered twice:
the executed calibration as `arithmetic-golden-ratio-receipt-calibration`
(external-calibration-record, home arithmetic, also a geometry reference) and
the presentations, plates and captured source as
`geometry-golden-ratio-external-reference`
(bounded-research-evidence, home geometry, lineage kind external-reference).

The geometry entry has no same-home parent chain to the Pascal root, so it is
not a candidate successor: admitted geometry successors remain zero and the
pinned growth obligation remains Open. Both entries pin the resource index, the
atlas, the bounded evidence, the research record, the frozen contract and the
checker. The read-only checker cannot pin the 15 staged artifacts
individually at 95 of its 96 files, so the per-artifact digests are enforced by
[`experiments/golden_ratio/calibration.py`](../../experiments/golden_ratio/calibration.py)
rather than by this catalog.

## Symbol surface swap companion

[Symbol surface swap v0](../meaning-symbol-surface-swap-v0.md) registers a
proposed logic-home reverse lookup view of Adva PR #170. Its eight source
files and nine open obligations survive unchanged. That addition grew the catalog to
17 entries; naming coverage was updated in both source and v1 documents.
This is documentary relation reordering, not native proof transport.

## Algebraic reconstruction trilogy

The al-Khwarizmi, Jiuzhang and Qin Jiushao proposed mappings extend the catalog
to 20 entries. The [finite CRT source-boundary calibration](../calibrations/crt-source-boundary-v0/README.md)
attached to the Qin Jiushao entry distinguishes unique reconstruction from
faithfulness to the declared source; it does not validate the historical prose.

## Nim rule-constraint typing

The `game` block of the [symbol surface](../symbol-surface/source/README.md) is
admitted as the entry `logic-nim-rule-constraint` (`logic`, proposed-document).
The typing is the direction's: the block is a **syntactic operation-rule
constraint**, not an arithmetic result and not a knowledge classification.

The reason is what the block already is. It carries registration, continuation
and fuel discipline, and it declares its own four rules missing — players, turn
order, legal move relation and winning condition. Rules are what the logic home
already holds. The nearest precedent is
`logic-cryptographic-sealing-and-calibration-boundary`: that entry **contains**
exact finite computation and its home is still logic, with arithmetic only
referencing the finite-computation discussion.

Three boundaries the entry states about itself:

- It does **not** claim that Nim is logic. ADR 0042 already fixes that a topic
  home is a documentary coordinate, not a classification of the subject, and the
  entry's `domains` lists `logic` alone rather than `[logic, arithmetic]` — the
  XOR criterion is an internal detail of a criterion, not the entry's kind.
- The pair 形上 / 形下 appears in the naming record as **borrowed descriptive
  vocabulary, not an authority**. The descending half of the crossing is not
  established either: `logic-as-research-content` already records that a semantic
  account of logic lowering remains unconstructed.
- Its four materials are the symbol-surface `presentation.json`,
  `obligations.json`, `contract.json` and `README.md`. The external Bouton
  criterion, the Sprague-Grundy normal form and the misère results are recorded
  as **declared imports only**: not pinned, not read in full, and supporting no
  import claim.

The entry supplies no game rules, no fuel allocation, no execution, search or
proof, and it changes no byte of the payloads. Its open obligations keep the game
name withheld, require any future name to come from this system's own rule
description rather than from the traditional game it resembles, and note that an
executable half would need its own home `arithmetic` entry with
`domains: [arithmetic, logic]`, mirroring `three-verifier-arithmetic-calibration`.
