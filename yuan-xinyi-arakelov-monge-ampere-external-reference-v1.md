# External reference, layer v1: the source-backed layer for the Arakelov / Monge–Ampère assessment

Status: `proposed-document`. This layer **appends** to
`yuan-xinyi-arakelov-monge-ampere-external-reference-v0.md`; it does not rewrite
it, and the v0 pin stays valid. Layer v0 remains the record of the supplied
reading and of the first assessment, including the parts this layer corrects.
Like v0, this is **not a derivation parent**, **not a semantic authority**, not a
claim, and not evidence; it has no checker and no run.

Same catalog entry:
`geometry-yuan-xinyi-arakelov-monge-ampere-external-reference`.

Why this layer exists: v0's two corrections rested on standard background that
had not been fetched, and v0 said so. Mingli Yuan asked on 2026-09-13 for those
corrections to be carried by sources rather than by assertion. This layer fetches
the author's own texts and re-checks each v0 statement against them.

**Result, stated first because it is the point: fetching the sources confirmed
one v0 correction, showed a second to be partly wrong, and showed a third to be
wrong in its second half.** The corrections of v0 are recorded below, not
quietly applied.

## 1. Sources read for this layer

The author's own publication page lists a PDF for each work; the four below were
downloaded on 2026-09-13 and converted to text with `pdftotext` (poppler). The
bytes are **not** retained in this repository — only their digests are recorded,
so that the reading is dated and identified but no third-party PDF is
redistributed here. Quotations below come from the extracted text; its
typography, hyphenation and symbol encoding are not reproduced (for example the
norm symbol appears as `k · k`).

| Source | File | Pages | SHA256 of the fetched bytes |
| --- | --- | ---: | --- |
| X. Yuan, *Adelic line bundles, arithmetic positivity and Diophantine geometry* (ICCM 2025) | `preprints/ICCM2025.pdf` | 73 | `98a31161aa0011baef7a8529e79fe9b8a32cdee99a0be4f31fd4edab1f4224b0` |
| X. Yuan, *On Faltings heights of abelian varieties with complex multiplication* (ICCM 2016) | `preprints/ICCM2016.pdf` | 17 | `d6ef9bf1a9cca95401eaa2dc813b1407e33e7e6a8d76da4a1f90d4d416e6113e` |
| X. Yuan, S.-W. Zhang, *The arithmetic Hodge index theorem for adelic line bundles* | `preprints/hodge_I.pdf` | 59 | `f4f8a6613793b68e67cb0e94da964f7d89a11a28589aaf53049a96431b3848f3` |
| X. Yuan, *Algebraic dynamics, canonical heights and Arakelov geometry* (ICCM 2010) | `preprints/ICCM2010.pdf` | 37 | `9ccd5d192da3877e90821a588f7815a9bb5e0521a5850fc3879feca2ccc8a765` |

The publication page states that its files "may be slightly different from the
published versions", so these are the author's posted versions, not certified
copies of the proceedings articles. The fourth file was searched but contributed
nothing to the findings below; it is listed because it was read for this layer.

Only `hodge_I` has an openly available arXiv counterpart (arXiv:1304.3538). The
two ICCM expositions do not, which is why their digests are recorded here.

## 2. What v0 said, and what the sources now support

### 2.1 Confirmed: the metric is input, not something solved for first

v0 §3 row 1 said the direction is reversed because in Arakelov geometry the
metric is part of the data. The ICCM 2025 text, §2, defines it exactly that way:

> An arithmetic divisor on X is a pair D = (D, g_D), where D is a Cartier divisor
> on X, and g_D is a Green function of D(C) on X(C), invariant under the action of
> complex conjugation.

The same section states the regularity required of that function:

> For the regularization of the Green function, we require that g_D : X(C) \
> |D(C)| −→ R is smooth, and that for any pair (U, f_U ) of an open subset U of
> X(C) together with a rational function f_U on U with div(f_U ) = D(C)|U , the
> function g_D + log |f_U | extends to a smooth …

and the adelic form:

> By a Green function of the divisor D on X an , we mean a continuous function
> g : X an \ |D|an → R with logarithmic singularity along D …

So the supplied reading's **first** claim ("we need to choose a canonical metric
before computing arithmetic intersections") is corrected as v0 said, and the
correction is now sourced: the Green function is a component of the arithmetic
divisor.

### 2.2 Partly wrong: what the "Faltings metric" is in this context

v0 said the Faltings metric is a Quillen metric on `det R^•f_*L`. That sentence
does not survive contact with the source that actually defines the height in
question. ICCM 2016 §2.2 defines the Faltings height of an abelian variety
through the **Hodge bundle**, with a metric given by an integral:

> The Hodge bundle of A is defined to be ωA = ε∗ ΩgA/OF = π∗ ΩgA/OF … There is a
> canonical hermitian metric k · k = {k · kσ }σ on ωA given by
> kαk2σ = (1/(2π)g) ∫Aσ (C) α ∧ ᾱ …

and then

> Define the unstable Faltings height of A to be h0 (A) = (1/[F : Q]) deg(ω A ).

The stable height is obtained by base change to semistable reduction. So in the
sense used here, the canonical metric in the Faltings height is **not** a
determinant-of-cohomology metric, and the word **"Quillen" occurs in none of the
four texts**. v0's det/Quillen sentence is therefore recorded as **unsourced** and
carried as an obligation, not as an established correction. What survives from
v0's row 1 is narrower and still useful: the supplied reading's example ("如
Faltings 度量") names an object that is not the canonical metric being solved for
on the manifold.

### 2.3 Wrong in its second half: Monge–Ampère *is* the route taken

v0 §3 row 2 concluded that solving Monge–Ampère "is not how this mathematician's
arithmetic results proceed". That half is wrong. The ICCM 2025 text, §6,
characterizes the canonical (admissible) metric precisely by an equality of
Monge–Ampère measures:

> We call the metric k · ka the admissible metric of ωC/F , which is actually nef
> (or semipositive). We call the Green function g∆ the admissible Green function
> of ∆ …

and

> By [Yua26a, Thm. A.1], there are a unique integrable metric k · ka of ωC/F on
> C an and a unique symmetric integrable metric k · k∆ of O(∆) on (C 2 )an
> satisfying the following: (1) the equality (2g − 2)c1 (O(x), k · kx ) =
> c1 (ωCF ′ /F ′ , k · ka ), of Monge–Ampère measures holds on (CF ′ )an ; (2) the
> integral …

with `[Yua26a]` resolved in that text's bibliography as *Arithmetic bigness and a
uniform Bogomolov-type result*, Ann. of Math. (2) 203 (2026), no. 1, 15–119. The
same text identifies which measure is meant:

> If v is complex (and X is projective), the measure is the classical Monge–
> Ampère measure on Xvan = Xv (C) in complex analysis by Bedford–Taylor [BT82].
> … If v is non-archimedean (and X is projective), the measure is the
> Chambert-Loir measure originally constructed by Chambert-Loir [CL06].

So the archimedean equilibrium measure in this framework **is** Bedford–Taylor's
complex Monge–Ampère measure, and the non-archimedean one is Chambert-Loir's.
v0's claim that Monge–Ampère is beside the point was an over-correction by this
registration, and it is retracted here. What remains true from v0 is narrower:
the canonical metrics are named as the Arakelov metrics in the complex case and as
metrics "essentially introduced by Zhang" in the non-archimedean case, so the
supplied reading's "典范度量（如 Faltings 度量）" still names the wrong example.

### 2.4 Upgraded: the regularity sentence is partially supported

v0 §3 row 2 called the supplied claim about pluripotential theory and the
regularity of weak solutions unsupported. That verdict is now **softened**, and
the supplied reading turns out to be closer to the sources than v0 allowed. In
`hodge_I`:

> For the equality part, we use a non-archimedean analogue of Blocki's method in
> [Bl], and the works of Gubler [Gu3] and Chambert-Loir–Thuillier [CT].

> One application of our local index theorem is the following non-archimedean
> analogue of the Calabi theorem. We refer to Calabi [Ca] for the original theorem
> and to Kolodziej [Ko] and Blocki [Bl] for some regularity extensions.

> There is an open problem about the existence of a metric on a line bundle with a
> given volume form, i.e., the non-archimedean analogue of the theorem of Yau
> [Ya]. Some partial results have been obtained by Liu [Li] and
> Boucksom–Favre–Jonsson [BFJ].

So the complex Monge–Ampère equation, its uniqueness and stability, and the
associated regularity literature are cited in his own work, and one of his
methods is explicitly modelled on Blocki's. What is still not established is the
supplied reading's stronger wording that the work **must** use pluripotential
theory to study the regularity and singularity of weak solutions: the results in
these texts are the arithmetic Hodge index theorem and a Calabi-type uniqueness
corollary, and no regularity theorem is claimed as an output.

### 2.5 Partly sourced: the Poisson-equation claim

v0 recorded the Green-function paragraph as "substantially right" but with the
"Poisson equation" phrasing as unsourced background. The word **"Poisson" occurs
in none of the four texts**, so v0 was right to flag the wording — but the
underlying content is present under another name. In `hodge_I`, Lemma 2.6 chooses
the canonical metric by solving a Laplacian equation:

> Lemma 2.6. There is a smooth metric k · k0 on M at archimedean places, unique up
> to scalars, such that the curvature form of M0 = (M, k · k0 ) on X(C) pointwise
> satisfies c1 (M0 )c1 (L1 ) · · · c1 (Ln−1 ) = 0 …

and its proof:

> Set Ω = c1 (L1 ) · · · c1 (Ln−1 ). Then the left-hand side is a scalar multiple of
> the Laplacian ∆φ with respect to Ω.

That is a linear equation with a source, solved for a potential, with the
solution unique up to a constant — the shape v0 described, in the author's own
notation, and with the "unique up to scalars" statement that v0's qualification
(ii) predicted. The name "Poisson" remains this registration's gloss.

## 3. Corrected summary, superseding v0's for practical use

An arithmetic divisor is a pair (divisor, Green function), so the archimedean
metric is input data; the Green function is smooth away from the divisor with a
prescribed logarithmic singularity. The canonical choices in play are the
Arakelov metrics in the complex case and Zhang's admissible metrics in the
non-archimedean case. For a relative curve, the admissible metric and the
admissible Green function are characterized (Yuan, Ann. of Math. 203 (2026),
Thm. A.1) by an equality of Monge–Ampère measures plus an integral normalization —
at the archimedean places that measure is Bedford–Taylor's complex Monge–Ampère
measure, non-archimedeanly it is Chambert-Loir's. Where a canonical metric must be
selected, the local problem reduces to a Laplacian equation with a source, with
the solution unique up to scalars. The non-archimedean Calabi–Yau statement is
reached through the arithmetic Hodge index theorem for adelic line bundles, and
Yau's theorem with the Blocki and Kołodziej regularity literature is cited as its
archimedean counterpart. So the supplied reading was **right that a canonical
metric is at stake and right that Monge–Ampère and Green functions are the
machinery**; it was wrong about the direction of the dependency, wrong about which
object "Faltings 度量" names in this context, and too strong in describing the
programme as a study of weak-solution regularity.

## 4. Unknowns and obligations carried forward

- **The det-of-cohomology / Quillen sentence is unsourced.** No fetched text
  contains the word "Quillen", and the height that ICCM 2016 defines uses the
  Hodge bundle instead. Whether some other construction in this body of work uses
  a Faltings–Quillen metric is not decided here.
- **"Poisson" is this registration's word**, not the sources'. The sourced
  statement is the Laplacian equation of `hodge_I` Lemma 2.6.
- **The programme question is still open.** The four texts were converted to text
  and searched; they were **not read end to end**, and no page-by-page reading is
  claimed. Whether a pluripotential-regularity programme exists elsewhere in this
  body of work is not decided.
- **Versions.** The two ICCM files are the author's posted preprints and his page
  warns they may differ from the published versions; `hodge_I` was read as the
  posted preprint, whose published form is Math. Ann. 367 (2017) 1123–1171.
- **The fetched bytes are not retained** in this repository, so the quotations
  cannot be re-verified against a pinned copy here; only the digests above are
  recorded.
- **The supplied message was truncated** at `###`, so further points may exist
  and are not recorded.
- Layer v0 is not corrected in place. Its two wrong or imprecise statements stay
  visible there, with this layer as the correction; that is deliberate, so a
  reader can see what was claimed before the sources were read.

## 5. Non-claims and reuse

No claim of this repository is made or changed here; nothing was re-derived, and
no equation was checked. The entry remains `proposed-document` with `checker:
null`, lineage `external-reference` (so it cannot be any candidate's derivation
parent, which the catalog checker enforces), and no native admission. Quote with
the entry pins, keep the source, version and layer attached, and cite the primary
text — not this file — for any mathematical statement. For the two ICCM
expositions, cite the published proceedings, not the posted preprint.
