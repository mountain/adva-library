# External reference: umbral moonshine and the K3 elliptic genus

Status: `proposed-document`. This is a documentary registration of external
literature. It is **not a derivation parent**, **not a semantic authority**, not a
claim of this repository, and not evidence for anything. It has no checker, no
run and no evidence file. Nothing mathematical below was re-derived, re-computed
or independently verified here.

Catalog home: one entry, key
`geometry-moonshine-k3-elliptic-genus-external-reference`, registered in
`math/manifest.json` with `geometry_lineage.kind = "external-reference"`.

Proposed by Mingli Yuan on 2026-09-13, with explicit instructions: record the
relation, carry sources, versions and unknowns, and mark it as neither a
derivation parent nor a semantic authority. Written and submitted by
deepseek-v4-flash-vision-exp (DeepSeek Harness) through his account as an
authorized proxy; he has not reviewed or endorsed it, and his name is not
evidence for any content here.

## 1. Why this file sits in `geometry`, and why the entry looks the way it does

The directory was chosen by **which checker enforces the required claim**, not by
topic — ADR 0043, axiom 1: *location grants nothing*.

- "Must not be a derivation parent" is enforced mechanically **only** for entries
  whose home is `geometry` and whose lineage kind is `external-reference`:
  `_lineage` in `python/adva/math_catalog.py` refuses derivation parents and
  derivation evidence for that kind, and `_geometry_graph` refuses to let an
  `external-reference` be the parent of any `candidate`. In every other home the
  same promise would be prose only.
- "Must not be a semantic authority" is enforced for **all** entries: the
  catalog's `policy` is fixed at `authority: documentary-only`,
  `native_admission: not-granted`, `logic_role: research-object-not-checker-override`,
  and the checker rejects a manifest that changes it.

That is the whole reason for both choices. The subject matter spans representation
theory, mock modular forms and string compactification; this entry makes no claim
about which topic it "really" belongs to, and it is not a statement about the
K3 surface, the Mathieu group, or string theory.

## 2. Sources, with the version each statement was read from

Every row was fetched on 2026-09-13. "How far it was read" says exactly how much
of the source backs this registration.

| Source | Version read | Identifiers | How far it was read |
| --- | --- | --- | --- |
| T. Eguchi, H. Ooguri, Y. Tachikawa, *Notes on the K3 Surface and the Mathieu group M₂₄* | arXiv v2 (submitted 2010-04-06), published version | arXiv:1004.0956; *Experimental Mathematics* 20 (2011) 91–96; DOI 10.1080/10586458.2011.544585 | abstract page and journal reference only |
| M. C. N. Cheng, J. F. R. Duncan, J. A. Harvey, *Umbral Moonshine* | published version, 2014 | arXiv:1204.2779; *Communications in Number Theory and Physics* 8 (2) 101–242; DOI 10.4310/cntp.2014.v8.n2.a1 | publisher record and abstract only |
| M. C. N. Cheng, J. F. R. Duncan, J. A. Harvey, *Umbral Moonshine and the Niemeier Lattices* | arXiv v1, 2013 | arXiv:1307.5793 | abstract page only; no journal reference is declared on that page |
| J. F. R. Duncan, M. J. Griffin, K. Ono, *Proof of the Umbral Moonshine Conjecture* | arXiv v2, 2015 | arXiv:1503.01472 | abstract page only; its comments say "to appear in Research in the Mathematical Sciences", which is not confirmed here |
| T. Gannon, *Much ado about Mathieu* | arXiv v2 revised 2013-03-15 | arXiv:1211.5531 | abstract page only; no published venue is confirmed here |
| V. Anagiannis, M. C. N. Cheng, S. M. Harrison, *K3 Elliptic Genus and an Umbral Moonshine Module* | published version, 2019 | *Communications in Mathematical Physics* 366 (2) 647–680; DOI 10.1007/s00220-019-03314-w | author's official publication list only; no arXiv identifier is confirmed here |
| M. C. N. Cheng, J. F. R. Duncan, *Optimal mock Jacobi theta functions* | published version, 2020 | *Advances in Mathematics* 372, article 107284 | author's official publication list only |
| M. C. N. Cheng, G. Sgroi, *Cone Vertex Algebras, Mock Theta Functions, and Umbral Moonshine Modules* | published version, 2025 | *Communications in Mathematical Physics* 406 (9), article 210; DOI 10.1007/s00220-025-05376-5 | author's official publication list only |

The primary institutional pages used are the author's official University of
Amsterdam publication list and the Institute of Mathematics, Academia Sinica
academic-staff listing; both were fetched on 2026-09-13.

## 3. The relation, as the sources state it

Everything in this section is **what a named source says**, quoted or
paraphrased, with the source named. None of it is asserted as this repository's
own result, and none of it was checked.

1. **The observation.** Eguchi–Ooguri–Tachikawa, verbatim: *"We point out that
   the elliptic genus of the K3 surface has a natural decomposition in terms of
   dimensions of irreducible representations of the largest Mathieu group M_24.
   The reason is yet a mystery."*
2. **The Mathieu case proved.** Gannon, verbatim: *"…we prove that the resulting
   sequence of class functions are true characters of M24, proving the
   Eguchi-Ooguri-Tachikawa conjecture. We prove the evenness property of the
   multiplicities, as conjectured by several authors."*
3. **The generalization to 23 cases.** Cheng–Duncan–Harvey relate umbral
   moonshine to the Niemeier lattices, verbatim: *"In this paper we relate umbral
   moonshine to the Niemeier lattices: the 23 even unimodular positive-definite
   lattices of rank 24 with non-trivial root systems. To each Niemeier lattice we
   attach a finite group by considering a naturally defined quotient of the
   lattice automorphism group, and for each conjugacy class of each of these
   groups we identify a vector-valued mock modular form whose components coincide
   with mock theta functions of Ramanujan in many cases."* The Mathieu case is
   stated in the companion paper to be recovered as a special case, and that paper
   describes the framework as relating automorphic forms, imaginary quadratic
   number fields, and six finite groups parameterized by the divisors of 12.
4. **Existence of the modules.** Duncan–Griffin–Ono, verbatim: *"The Umbral
   Moonshine Conjectures assert that there are infinite-dimensional graded
   modules, for prescribed finite groups, whose McKay-Thompson series are certain
   distinguished mock modular forms. Gannon has proved this for the special case
   involving the largest sporadic simple Mathieu group. Here we establish the
   existence of the umbral moonshine modules in the remaining 22 cases."*
5. **The K3-side module.** Anagiannis–Cheng–Harrison is recorded by its authors
   as constructing a module for the Mathieu case from the K3 elliptic genus. The
   later *Optimal mock Jacobi theta functions* and *Cone Vertex Algebras, Mock
   Theta Functions, and Umbral Moonshine Modules* continue the same line at the
   date of the publication list above.

Compressed to one sentence this registration says: **a distinguished family of
mock modular forms is indexed by the 23 Niemeier lattices, and the K3 elliptic
genus is the case that carries the largest Mathieu group, whose moonshine was
observed first and proved first.** That sentence is this registration's own
summary of the quoted statements, not a theorem, and it is the one thing here
most likely to be an oversimplification.

## 4. Unknowns and what was not verified

- **No full text was read.** Every row in section 2 says how far the reading
  went; several rows stop at an abstract page.
- **No number was checked.** In particular no coefficient sequence, no weight and
  index convention for the relevant Jacobi or mock modular forms, and no
  character table entry is reproduced here, quoted or otherwise, precisely
  because nothing was verified. A reader who needs a number must go to the source.
- **The count "23" is quoted, not derived.** It comes from the Niemeier-lattices
  abstract, which counts the rank-24 even unimodular positive-definite lattices
  with non-trivial root systems; the Duncan–Griffin–Ono abstract independently
  says "the remaining 22 cases" after the Mathieu one. Whether those two counts
  are the same count under the same convention is not established here.
- **Conventions differ between sources**, and this registration does not
  translate between them. Notations such as the elliptic genus normalization,
  the N=4 character decomposition, and the naming of the mock modular forms are
  source-local.
- **Versions drift.** arXiv v1 and the published version can differ; the table
  records which one was read, and the publication data for Gannon, for the
  Niemeier-lattices paper, and for Duncan–Griffin–Ono is incomplete here.
- **The author's own survey was not used as a source.** The 2022 Chinese
  interview in 數學傳播 was seen only as a search result; it is cited in the
  conversation that produced this proposal, not in this registration.

## 5. What this entry is not

- **Not a derivation parent.** Enforced: lineage kind `external-reference`, empty
  parents, empty derivation evidence, and a graph check that bars it from being
  any candidate's parent. It is also not a Pascal descendant, and the
  directory-separated growth obligation stays `Open` with no native `Seal`: this
  entry adds no geometry successor.
- **That refusal was verified, not assumed.** On 2026-09-13, on a copy of the
  catalog in a temporary directory, two candidate entries were appended: one
  naming this entry as its parent, and one naming the Pascal root. The first is
  refused — `InvalidCatalog`, `geometry parents must precede it and descend from
  Pascal in geometry` — while the second is accepted with `CatalogConsistent`, so
  the rule is not a machine that refuses every candidate. No repository file was
  mutated to produce those two rows.
- **Not a semantic authority.** The catalog's fixed policy is `documentary-only`
  with `native_admission: not-granted`; a digest here records byte integrity
  only, never authentication, semantic identity or proof. Registering a document
  changes what may be *cited*, not what is *true*.
- **Not a claim and not a checked result.** `recorded_status` is
  `proposed-document`, `checker` is `null`, and `evidence` is empty, so no
  executable claim is introduced. Nothing here is registered in
  `docs/claims.toml`, whose statuses admit no proposed state.
- **Not connected to anything in this repository.** `moonshine`, `umbral` and
  `Mathieu` have no other occurrence in `adva` or `adva-library` as of
  2026-09-13, so this entry has no dependency and can break none.
- **Not an interface.** Using any of this in a bounded trial would first require
  the six-part contract of Research 0129 §3, including the interface
  justification for whatever would be translated, and its own checker. This
  registration authorizes no such translation and supplies none.

## 6. Reuse

Quote with the entry pins, keep the source and version attached, and keep the
external-reference status attached. Do not cite this file for a mathematical
statement; cite the primary sources of section 2 for that. If a later document
wants to make a mathematical claim out of this material, that claim needs its own
checker, its own finite scope and its own residual, and it may still not treat
this entry as a derivation parent.
