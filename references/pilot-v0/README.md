# Executable content-reference pilot v0

Original integration by ChatGPT (OpenAI), contributed under Unknown v0.3,
submitted through Mingli Yuan's authorized account proxy; no personal authorship,
review, endorsement or correctness guarantee is implied.

This standalone content interface checks the actual immutable source bytes of
three existing original project documents. It does not start Adva, Rust, Lean,
Metamath or a native verification service. Python 3.11+, Git with
`--no-lazy-fetch`, and separately installed jsonschema 4.25.1 are required.
No third-party dependency source is bundled. No network request, installation,
Git fetch, fallback to HEAD or recursive dependency traversal occurs at runtime.

```sh
python -m pip install jsonschema==4.25.1
# Select this historical content revision independently of the manifest.
timeout 30s python references/pilot-v0/check_references.py \
  --checkout . --commit 19cede9c4532b7abd85f200daf7a9611a84563f0
timeout 60s python -m unittest discover -s references/pilot-v0 -v
```

Installation is separate from the offline invocation. An unsupported Git returns
Unknown; it never retries without the lazy-fetch guard. A shallow clone lacking
the exact source revision returns Unknown until the operator explicitly supplies
those Git objects. A timeout or incomplete report is never acceptance.

## Source identity and one home

| View ID | Exact source path at the selected library revision | Existing home |
| --- | --- | --- |
| library-boundary | README.md | repository entry point |
| topic-catalog | math/README.md | existing documentary catalog guide |
| symbol-view | meaning-symbol-surface-swap-v0.md | logic; logic-symbol-surface-swap |

`manifest.json` is a navigation view over those original documents, not another
catalog or owning topic. No payload or math entry is moved, copied into another
topic, added, renumbered or semantically promoted. Existing catalog pins, topic
counts, Pascal-rooted growth obligation and historical evidence are unchanged.
`source-digests.json` is a separately selected byte inventory. The caller supplies
the library commit; the manifest cannot select it. Digests establish integrity,
not source authentication, rights, semantic identity or proof.

Material sources are coordinates. Associative relations connect documentary
views. Trail order records a reading/research itinerary, and origin records a
branch from another itinerary; it is not proof ancestry. Two source-backed trails
run boundary-first and proposal-first. Computation dependencies and proof
premises are rejected by this library-only receiver. The proposal's historical
claims and dates are preserved as source bytes, not asserted to describe current
PR status. Reading these documents does not traverse or publish their linked
third-party inputs or execute their archived scripts.

## Machine implementation selection

`machine-pin.json` records full commit
`mountain/adva-machine@089c5ab8ec5f04768d03a377d0180e942fd77216`, source paths,
Git blob IDs, SHA-256 and sizes of six first-party files. `machine/` retains their
exact reviewed bytes and original attribution. These are schema, checker,
reference resolver, draft-profile README/proposal, and KPB v0.1 contract.
The integration checks independently embedded SHA-256 pins before importing
machine Python code. A manifest-supplied implementation cannot replace them.
This is a local draft implementation byte selection, not a stable release,
registry, native loader or upgrade of any upstream consumer lock.

The local publication record covers these first-party imports. Project-original
navigation and tests use the existing Unknown contribution policy. No external
texts, diagrams, datasets or dependency sources are imported.

## Receiving and finite bounds

| Result | Exit | Meaning |
| --- | ---: | --- |
| ReferenceBytesLocated | 0 | All distinct declared material/provenance sources located and SHA-256 checked |
| Rejected | 2 | Invalid manifest, missing source/digest pin, revision/digest mismatch or forbidden relation |
| Unknown | 3 | Required unknown extension, unavailable local bytes/dependency/toolchain or exhausted budget |

Optional unknown extensions remain opaque and are explicitly reported as ignored;
required unknown extensions block acceptance. Every result retains
`semantic_verification=NotRun`, `native_admission=NotGranted`, `native_launches=0`.
The separately pinned source contract is checked as implementation bytes, not a
native proof premise. CLI JSON is documentary output, not an admission token.

Bounds: 64 KiB per manifest/digest/schema/source blob, schema limits of 32 nodes,
64 relations and 8 trails; at most 264 source occurrences and 256 digest pins;
10-second aggregate cooperative deadline including imports and byte checking,
with remaining time supplied to each Git lookup. The external 30-second watchdog
covers startup and output too. No memory ceiling is enforced. As in the machine
pilot, checkout metadata and bounded Git command output are trusted; this is not
a hostile-checkout sandbox. Git calls never execute source material.

The 15 test methods cover actual three-document success, missing source/local
bytes, incompatible version, digest mismatch, required/optional unknown extension,
zero budget, missing independent pin, machine byte tampering, dangling trail,
source-contract mismatch, and two forbidden relation kinds. These are finite
controls, not universal compatibility or semantic validation.

## Remaining adoption gates

Implemented: local documentary interface and content-side manifest/byte lookup.
Still incomplete: formal consumer adoption in adva/adva-machine, their dependency
lock selection, an independently bound receiving/effects contract, authenticated
custody where required, actual KPB-14 consumer migration, migration refusal checks
and native admission/reverification. This pilot completes neither KPB-14 nor a
new native package boundary. A successor must select its own exact library and
machine bytes and rerun checks; this tool never repairs pins automatically.
