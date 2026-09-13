# External reference: 袁新意 (Xinyi Yuan) on Arakelov geometry, and a supplied reading of his relation to Monge–Ampère

Status: `proposed-document`. This is a documentary registration of external
literature and of one supplied reading of it. It is **not a derivation parent**,
**not a semantic authority**, not a claim of this repository, and not evidence
for anything. It has no checker, no run and no evidence file.

Catalog home: one entry, key
`geometry-yuan-xinyi-arakelov-monge-ampere-external-reference`, registered in
`math/manifest.json` with `geometry_lineage.kind = "external-reference"`. The
home follows ADR 0043 axiom 1 (location grants nothing): it is the only home in
which the catalog checker mechanically refuses derivation parents for an external
reference.

Proposed by Mingli Yuan on 2026-09-13, who supplied the reading in section 1 and
asked that it be registered with corrections and with the corrected readings
retained. Written and submitted by deepseek-v4-flash-vision-exp (DeepSeek
Harness) through his account as an authorized proxy; he has not reviewed or
endorsed it, and his name is not evidence for any content here.

## 0. What was received, and what this registration does

The direction sent a two-paragraph summary of the relation between this
mathematician's work and two PDE questions, under the heading "我们看如下来自
袁心意教授的工作". The message ended with `###` and appears to have been
truncated; only the two paragraphs below were received, and no third point is
recorded here because none arrived.

This registration does three things: it keeps the supplied reading verbatim as
the object being assessed, it records a corrected reading with the sources that
support it, and it records the two readings it finds wrong **without deleting
them**, so that a later reader can see what was corrected and why.

The supplied name is written 袁心意; the person is 袁新意 (Xinyi Yuan). The
spelling is recorded as received and is not rewritten in the quotation.

## 1. The supplied reading, verbatim

> 1. **复 Monge-Ampère 方程（完全非线性椭圆 PDE）：**
>
>    在计算算术相交数时，我们需要在复流形上选取"典范度量"（Canonical metrics，如 Faltings 度量）。寻找这种度量，本质上就是求解复 Monge-Ampère 方程。袁新意等人在处理高维算术代数几何时，必须借助多势论（Pluripotential theory）来研究这些非线性 PDE 弱解的正则性和奇异性。
>
> 2. **格林函数与电流（Green's Currents）：**
>
>    Arakelov 几何中的除子相交，依赖于构造具有特定奇异性的格林函数，这需要解泊松方程（最经典的线性 PDE）。

Its provenance is not recorded: whether it was written by the direction or
produced elsewhere and forwarded is unknown, and no author is asserted here.

## 2. Sources, with the version each statement was read from

Every row was fetched on 2026-09-13.

| Source | Version read | How far it was read |
| --- | --- | --- |
| 袁新意 official publication list, BICMR/PKU | page as served on that date | read in full; it is the basis for the work list in section 4 |
| 北京大学新闻网, "北京国际数学研究中心袁新意教授荣获2026未来科学大奖" | 2026-08-13 | read in full |
| X. Yuan, S.-W. Zhang, *The arithmetic Hodge index theorem for adelic line bundles I* | arXiv:1304.3538, v1 | abstract page only |
| X. Yuan, *On volumes of arithmetic line bundles* | arXiv:0811.0226, v2; published *Compositio Mathematica* 145 (2009) 1447–1464 | abstract page only |

No full text of any paper was read, and no theorem below was re-derived.

## 3. Claim-by-claim assessment

"依据" says what backs the assessment: a fetched source, or standard background
that this registration states as its own reading and did **not** re-verify.

| Supplied claim | Verdict | Corrected statement | 依据 |
| --- | --- | --- | --- |
| 计算算术相交数时需要先选取"典范度量"（如 Faltings 度量） | Reversed, and the example is the wrong object | In Arakelov geometry the metric is **input**, not something solved for first: an arithmetic divisor is a pair (divisor, Green function/metric), and the intersection pairing is defined from that data. Separately, the Faltings metric lives on det R^•f_*L and is a Quillen metric built from a zeta-regularized determinant; it is not a canonical metric obtained by solving a Monge–Ampère equation on the manifold. The canonical metrics of the theory are, for instance, the Arakelov metric on a curve and the admissible metric on an abelian variety. | standard background; this registration's reading, not re-verified here |
| 寻找这种度量本质上就是求解复 Monge–Ampère 方程 | True for canonical/Kähler–Einstein metrics, not the route taken here | For Kähler–Einstein metrics this is exactly the complex Monge–Ampère equation (Calabi conjecture, Yau; Aubin–Yau), and in complex dimension one the Arakelov metric is a solution of a Liouville-type equation. It is not how this mathematician's arithmetic results proceed. | standard background; this registration's reading |
| 袁新意等人必须借助多势论研究这些非线性 PDE 弱解的正则性和奇异性 | Not supported | No such programme appears in the work list. The Monge–Ampère connection in this work is the **non-archimedean** Calabi–Yau theorem, whose uniqueness part is obtained as a consequence of the arithmetic Hodge index theorem for adelic line bundles: the abstract says "we obtain the uniqueness part of the non-archimedean Calabi--Yau theorem". That is non-archimedean (Berkovich-theoretic) Monge–Ampère, a different theory from the regularity of weak solutions of the complex equation. The volume and positivity work instead goes through arithmetic Okounkov bodies and the arithmetic Hilbert–Samuel theorem. | arXiv:1304.3538 and arXiv:0811.0226 abstracts; official publication list |
| Arakelov 几何中的除子相交依赖构造具有特定奇异性的格林函数，这需要解泊松方程 | Substantially right, with three qualifications | Correct: arithmetic intersection theory pairs divisors with Green currents. Qualifications: (i) the equation is `d d^c g + δ_D = [ω]`, a current equation whose right-hand side is a measure, so it is a Poisson equation in the distributional sense with a prescribed logarithmic singularity; (ii) on a compact manifold the solution is unique only up to a constant, subject to the compatibility `deg D = ∫ω`; (iii) Arakelov geometry does not need to *solve* for a Green function — it is part of the arithmetic divisor — one solves when a *canonical* choice is wanted. The genuine link to this mathematician's work is the Faltings–Hriljac–Moriwaki arithmetic Hodge index theorem, which relates arithmetic self-intersections to Néron–Tate heights through Green functions; the adelic version "extends the arithmetic Hodge index theorem of Faltings, Hriljac and Moriwaki on arithmetic varieties". | standard background for (i)–(iii); arXiv:1304.3538 abstract for the link |

Summary: **the second paragraph is essentially right, the first paragraph has a
reversed direction, one wrong object, and one sentence that the sources do not
support.**

## 4. The corrected reading

The work is in number theory and arithmetic geometry, along Arakelov geometry,
Diophantine geometry, arithmetic dynamics, Shimura varieties and L-functions. The
recorded items, as the official publication list gives them, include: *Big line
bundles over arithmetic varieties* (Inventiones 173, 2008); *On volumes of
arithmetic line bundles* (Compositio 145, 2009) and *Volumes of arithmetic
Okounkov bodies* (Math. Z. 280, 2015); the arithmetic Hodge index theorem for
adelic line bundles (with S.-W. Zhang, Math. Ann. 367, 2017), whose sequel treats
finitely generated fields (2021) and whose framework is the book *Adelic line
bundles on quasi-projective varieties* (Annals of Mathematics Studies, 2026);
*Arithmetic bigness and a uniform Bogomolov-type result* (Ann. of Math. 203,
2026); the geometric Bogomolov conjecture in arbitrary characteristics (with J.
Xie, Invent. Math. 229, 2022) and work on the geometric Bombieri–Lang conjecture;
and, on the automorphic side, the averaged Colmez conjecture (with S.-W. Zhang,
Ann. of Math. 187, 2018).

The university's own notice of the 2026 Future Science Prize states the citation
verbatim as 表彰他"在算术几何领域作出的奠基性贡献，特别是创立了 Arakelov 几何中的
算术大性理论，并将其开创性地应用于一致 Bogomolov 猜想和一致 Mordell 猜想"，and
records an invited 45-minute lecture at the 2026 International Congress of
Mathematicians.

Where Monge–Ampère actually enters is narrow and specific: as the non-archimedean
Calabi–Yau statement reached through the adelic Hodge index theorem. Where Green
functions actually enter is broad and central: they are the archimedean half of
the arithmetic intersection pairing, and the arithmetic Hodge index theorem is
exactly the place where they meet heights.

## 5. Unknowns and what was not verified

- **No full text was read.** Two papers were read only through abstract pages,
  and the publication list is a list.
- **The corrections are this registration's reading of standard Arakelov
  theory**, not re-derived results; no source was fetched to support the
  statements about the Arakelov metric, the admissible metric, the Quillen
  metric or the Green-current equation. They are recorded as an assessment and
  are open to correction on the same terms as anything else here.
- **The absence of a pluripotential-regularity programme is an argument from the
  publication list, not a proof of absence.** A paper not listed, a preprint not
  seen, or a lecture not recorded would change it.
- **The supplied reading's provenance is unknown** (see section 1), and the
  message was truncated, so the two paragraphs may be part of a longer list.
- **No number, theorem statement, or citation inside the papers was checked**;
  the quotations in section 3 are abstract-page text.

## 6. What this entry is not

- **Not a derivation parent.** Enforced by the catalog: lineage kind
  `external-reference`, empty parents, empty derivation evidence, and a graph
  check that bars it from being any candidate's parent. It is not a Pascal
  descendant, and the growth obligation stays `Open` with no native `Seal`.
- **Not a semantic authority.** The catalog policy is fixed at
  `documentary-only` with `native_admission: not-granted`; a digest records byte
  integrity only. Registering a document changes what may be cited, not what is
  true.
- **Not a claim and not a checked result.** `recorded_status` is
  `proposed-document`, `checker` is `null`, `evidence` is empty, and nothing is
  added to `docs/claims.toml`.
- **Not connected to any existing record.** The name 袁新意 / Xinyi Yuan occurs
  nowhere else in `adva` or `adva-library` as of 2026-09-13. The neighbouring
  record is
  [`../docs/research/0169-arakelov-stability-monge-ampere-mirror-ladder.md`](../docs/research/0169-arakelov-stability-monge-ampere-mirror-ladder.md),
  which is a bounded experiment of this repository on Arakelov-adjacent material
  and is not extended, imported or cited as authority by this entry.
- **Not an interface.** Any use in a bounded trial needs its own six-part
  contract under Research 0129 §3, its own checker and its own residual.

## 7. Reuse

Quote with the entry pins, keep the source and version attached, and keep the
external-reference status attached. For a mathematical statement, cite the
primary source, not this file. The two corrected readings in section 3 are
retained deliberately: a later reader who meets the same two sentences should be
able to see both the sentence and its correction in one place.
