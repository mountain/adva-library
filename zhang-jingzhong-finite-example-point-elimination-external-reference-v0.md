# External reference: Zhang Jingzhong on the finite-example method and point elimination

- Registration kind: external reference, documentary only
- Recorded status: proposed document
- Catalog home: `geometry`, lineage `external-reference`
- Date of the readings: 2026-09-13
- Origin: proposed by Mingli Yuan with the request quoted in section 1, for a study of
  whether these methods act on the statements this repository already carries

This file registers external literature. **No mathematical statement in it was
re-derived, recomputed or independently verified here**, and no full text was read.
Each section records how far its reading went, so that a reader can tell a fetched
sentence from a citation of a citation.

## 1. What was asked

> 我在想沿着吴文俊先生的路径，https://zh.wikipedia.org/zh-cn/张景中 张景中先生的有限例证方法和我们的思考非常的接近，还有他很独特的 消点算法 ，我们找一下资料研究一下

The request names the Chinese Wikipedia entry; that entry was **not retrievable** on
this host (two fetches, including `action=raw`, returned empty responses). Everything
below therefore comes from institutional pages, a journal page and a bibliographic
database that were fetched, and the unretrieved item is recorded as unretrieved rather
than paraphrased.

## 2. Sources, with how far each reading went

### 2.1 Institute page: attribution and naming

`http://www.casit.ac.cn/jianjie/107.html`, 中国科学院成都计算机应用研究所研究生教育网,
导师简介 page for 张景中, fetched 2026-09-13. Read: the full page.

> 1990 年张景中、杨路提出了定理机器证明的数值并行方法，在世界上首次用计算机实现了有严密理论依据的几何定理例证法。方法优点之一是占用内存小，至今是唯一可用袖珍计算机证明非平凡几何定理的方法，也是机器证明中唯一可高度并行的算法。在国外文献中称此法为"张杨定理"。用此法发现的新定理引起国外专文讨论。

> 1992 年张景中等提出了几何定理可读证明自动生成的理论、算法和方法，并实现为通用的微机程序。用此新方法已经证明近千个非平凡的几何定理，其中有几十个非欧几何的新定理，对多数定理计算机自动生成了简捷优美的证明……以此成果为主的项目获中国科学院 1995 年自然科学一等奖，1997 年国家自然科学二等奖。

This is the institute's own page. The 1990 date, the binding of 例证法 to the
numerical parallel method, the small-memory and parallel character, and the foreign
name "Zhang-Yang theorem" are recorded **as that page states them**. No independent
confirmation of the foreign naming was obtained.

### 2.2 University page: the contribution list

`https://hp.gzhu.edu.cn/info/1184/1025.htm`, 广州大学黄埔研究院 院士页 for 张景中,
fetched 2026-09-13. Read: the full page.

> （1）提出以面积方法为基础的消点法，实现了几何定理可读证明的自动生成，使计算能够给出容易理解和检验的推理演算或证明过程……
> （2）提出用检验有限个实例证明几何定理的"数值并行法"；（3）提出处理代数方程组的"WR 分解算法"和"弱非退化条件"算法，改进了吴法；（4）提出用近似计算获取准确值的理论和基本方法……

The same page lists, under 动力系统与迭代, "给出费根堡函数方程连续解构造方法". That is
the same object as this repository's Feigenbaum line (notes 0176–0180) and is recorded
here **as a cross-identification only**; nothing about it is derived here.

The clause worth preserving verbatim is item (3): a **weak non-degeneracy condition**
algorithm that improves Wu's method. This repository's Wu rounds (0181, 0182) had to
record a non-degeneracy condition explicitly, so the clause points at the same
question. The algorithm's own text was **not read**, and the clause is carried as a
lead and not as support.

### 2.3 Bibliographic database: the two records

zbMATH Open API, fetched 2026-09-13. Read: bibliographic fields only.

| Identifier | Record |
| --- | --- |
| Zbl 0648.68096 | Zhang, Jingzhong; Yang, Lu; Deng, Mike, *The parallel numerical method of mechanical theorem proving*, Res. Rep., Math. Sci. **30**, 16 p. (1988), Institute of Mathematical Sciences, Chengdu Branch of Academia Sinica; MSC 51M05, 12E05, 68W30, 68T99, 03B45 |
| Zbl 0701.68087 | Same title, *Theoretical Computer Science* **74**(3), 253–271 (1990), DOI `10.1016/0304-3975(90)90077-U`; MSC 68T15, 03B35 |

The zbMATH review text is not retrievable: the API returns
`contents unavailable due to conflicting licenses`. So the records above are
bibliographic, and **no review content is quoted**.

### 2.4 Journal page: the earlier name

`https://wap.cnki.net/touch/web/Journal/Article/STYS198901004.html`, 王东明,
《例证法与代数簇的包含关系》,《系统科学与数学》1989 年第 1 期, fetched 2026-09-13.
Read: the abstract only.

> 1986 年，洪加威教授发展吴文俊机器证明理论，提出了一类平面几何定理的例证法，这一方法依赖于 Ritt-吴整序原理和吴文俊教授关于升组不可约分解的构造性理论。我们发现例证法适用于证明所有等式型几何定理，即吴几何中的定理。

This page is the basis for recording that the name 例证法 has an earlier layer
(洪加威 1986, on Wu's route) distinct from the 1990 numerical realisation attributed to
张景中 and 杨路 in section 2.1. The two layers are kept apart here; the full texts were
not read.

### 2.5 Coq formalisation: the executable vocabulary of the point-elimination method

`https://www.irif.fr/~narboux/area_method.html`, Julien Narboux, formalisation of the
area method of Chou–Gao–Zhang, *Machine Proofs in Geometry*, World Scientific, 1994.
Fetched 2026-09-13. Read: the full page.

The page states the method's shape: express the theorem as a sequence of geometric
constructions, then treat the points in the **reverse order of their construction**,
eliminating every occurrence of each constructed point through elimination lemmas (for
areas, for ratios, for Pythagoras differences); when only free points remain, the goal
is decided by field arithmetic. It lists the constructions (`on_line`, `on_line_d`,
`inter_ll`, `on_parallel(_d)`, `on_inter_line_parallel`, `on_inter_parallel_parallel`,
`is_midpoint`, `on_perp(_d)`, `on_inter_line_perp`, `is_circumcenter`, `is_orthocenter`,
`is_centroid`), the three quantities the goal may use (a ratio of oriented distances, a
signed triangle area, a Pythagoras difference `AB² + BC² − AC²`), the permitted goal
predicates, and a list of theorems the development proves that includes Ceva,
Desargues, Menelaus, Pappus, Pascal's axiom, the Gauss line, the nine-point circle and
the Euler line. It also cites "The Area Method: a recapitulation" (with Janicic and
Quaresma) as a further reference; **that paper itself was not fetched**.

The overlap with this repository is exact: 0181 and 0182 carried Ceva, Pappus and
Pascal by Wu's method, and this page lists the same statements as the area method's
targets. The two methods are different objects — one produces a polynomial remainder,
the other a readable sequence of elimination steps — and they are not merged here.

## 3. Not retrieved

- The Chinese Wikipedia entry for 张景中 (empty responses; recorded as unretrieved).
- The zbMATH review text (licence-blocked).
- The full texts of Hong Jiawei 1986, Wang Dongming 1989, Zhang–Yang–Deng 1988/1990,
  Chou–Gao–Zhang 1994, and the area-method recapitulation.
- Any original statement of the a priori degree-bound theory that makes the
  finite-example method sound for a general statement class. Only the institutional
  sentence "有严密理论依据" (with a rigorous theoretical basis) was read; the argument
  behind it was not.

## 4. Relation to this repository's own run

`docs/research/0183-zhang-finite-example-verification.md` and
`experiments/zhang_finite_example/` test the finite-example criterion itself, on
statements this repository already carries, with its own frozen contract, checker and
residual. That run is **not** evidence for anything in this registration, and this
registration is not authority for that run: the run cites section 2 here for what the
sources say, and answers for its own measurements itself. The point-elimination half is
a separate declared experiment and is not covered by either file.

## 5. Open obligations

- No checker, no evidence file and no executed run: this entry introduces no executable
  claim and changes nothing in `docs/claims.toml`.
- The attribution layering (1986 洪加威, 1990 张景中–杨路) rests on one abstract and one
  institute page. A reader who needs the priority must go to the primary texts.
- The foreign name "Zhang-Yang theorem" is the institute page's claim; no
  English-language source confirming that usage was fetched.
- Nothing was verified about the method's soundness, its complexity, its bound theory,
  or the pocket-calculator and thousand-theorem performance claims, all of which are
  quoted from institutional pages rather than checked.
- The clause about a weak non-degeneracy condition improving Wu's method is unresolved
  by this reading, and this repository's own non-degeneracy observations remain its own.

## 6. Explicit non-claims

- This is a documentary registration, not a derivation parent, not a Pascal descendant,
  not a growth-obligation successor, and not a semantic authority.
- It grants no native admission, no Seal and no geometry catalog successor; the
  Pascal-rooted growth obligation stays Open.
- It does not claim that the finite-example method or the point-elimination method is
  correct, complete, or applicable to any statement outside the ones this repository
  runs.
- No priority, no historical completeness and no bibliographic completeness is claimed.
