# External reference: Yang Lu on inequality proving and machine discovery

- Registration kind: external reference, documentary only
- Recorded status: proposed document
- Catalog home: `geometry`, lineage `external-reference`
- Date of the readings: 2026-09-13
- Origin: proposed by Mingli Yuan, asking to analyse Yang Lu's theory of inequalities, in
  the same session and by the same route as the registration of Zhang Jingzhong
- Admission history: the first attempt at this registration was reverted because the
  catalog had reached its declared entries bound exactly and the growth fixture that
  keeps growth and naming in step had no headroom left. The direction then gave the bound
  its own reason — 我设立 100 条，必须让小朋友跑出来 — and `LIMITS["entries"]` moved from 32
  to 101, which is 100 entries plus the one the fixture appends. This document is the
  registration admitted under that bound. The attempt, the revert and the resolution are
  recorded in `docs/research/yang-lu-reference-registration-deferred.md`.

This file registers external literature. **No mathematical statement in it was
re-derived, recomputed or independently verified here**, and no full text was read. Each
reading records how far it went, so that a stated sentence can be told apart from a
citation of a citation.

## 1. What was asked

> 在吴文俊先生传人中还有一个 杨路 先生 … 张景中、杨路他们这一级数力系被称为是北大数学的第一个黄金一代，但毕生坎坷。下面我们重点分析一下杨路先生关于不等式的理论。

The Chinese Wikipedia entry for Zhang Jingzhong was unretrievable in the earlier round and
the Baidu entry for Yang Lu named here returns "百度安全验证" on this host, so neither is a
source for anything below.

The user's framing of the two as one cohort is **not** corroborated by any source read
here, and it is not repeated as a fact. What can be checked is one coincidence of dates:
the institute page for Zhang Jingzhong records 1959 graduation from the Department of
Mathematics and Mechanics at Peking University, and the institute page for Yang Lu records
1959 graduation from the Department of Mathematics at the same university.

## 2. Readings

### 2.1 Institute page: his own programme

`http://www.casit.ac.cn/jianjie/106.html`, 中国科学院成都计算机应用研究所研究生教育网, 导师简介 page
for 杨路, fetched 2026-09-13. Read: the full page.

> 1.1959 年毕业于北京大学数学系。 2. 研究员、计算机软件与理论博士生导师、数学博士生导师。 3. 中国科学院"不等式机器证明与机器发现"知识创新项目首席科学家。 4. 国家 973 项目"数学机械化与自动推理平台"（G1998040600）专家委员会成员。 5. 国家 973 项目"构造性实代数几何与不等式自动推理"（G1998030602）主持人。

> 1993 年 任 IMO 中国国家代表队领队、主教练。

> 1.1995 年获中国科学院自然科学一等奖。2.1997 年获国家自然科学二等奖。3.2001 年获中国第 8 届专利博览会金奖。4.2003 年获全国"五一"劳动奖章。

The page places inequality proving under a project **he** was chief scientist of, so the
subject is recorded here as a line of his own rather than as a by-product of the joint work
with Zhang Jingzhong. The 1995 and 1997 awards are the same two the Zhang Jingzhong page
records, which is consistent with the two sharing that period's results; the 2001
patent-exhibition gold medal is the entry that corresponds to software.

### 2.2 Journal abstract: the method, the program and its benchmark

`http://cjc.ict.ac.cn/eng/qwjse/view.asp?id=1283`, Chinese Journal of Computers (计算机学报),
2003, No. 7, 769–778, YANG Lu and XIA Shi-Hong, "Automated Proving for a Class of
Constructive Geometric Inequalities". Fetched 2026-09-13. Read: the English abstract and
keywords.

> An automated inequality-proving algorithm is presented based on a mixed method including a so-called cell-decomposition. That is implemented by a Maple program named "BOTTEMA" which can prove or disprove propositions in an extensive class of geometric and algebraic inequalities involving radicals. Most of the theorems in "Geometric Inequalities" writed by Bottema et al., can be proven efficiently in this way.

Keywords: automated proving, geometric inequality, cell-decomposition, semi-algebraic
system.

This is the strongest single reading obtained: the name of the approach (a mixed method
including a cell-decomposition), the program (BOTTEMA, a Maple program), its declared reach
(a wide class of geometric and algebraic inequalities involving radicals) and its benchmark
(most theorems in Bottema et al.'s *Geometric Inequalities*). The abstract also says the
program **can prove or disprove**, a capability that this repository's own bounded trial of
a related certificate does not have, where a statement that is not proved stays `Unknown`.

### 2.3 Bibliographic records

zbMATH Open API, fetched 2026-09-13. Read: bibliographic fields only.

| Identifier | Record |
| --- | --- |
| Zbl 1362.26001 | Xia, Bican; Yang, Lu, *Automated inequality proving and discovering*, Hackensack, NJ: World Scientific (2016), ISBN 978-981-4759-11-3 / 978-981-4759-13-7, xii + 332 pp.; MSC 26-02, 68-02, 26D05, 03B35 |
| Zbl 0648.68096 | Zhang, Jingzhong; Yang, Lu; Deng, Mike, *The parallel numerical method of mechanical theorem proving*, Res. Rep., Math. Sci. 30, 16 p. (1988) — already registered in the Zhang Jingzhong entry, recorded here because Yang Lu is the second author |
| Zbl 0701.68087 | The same paper in *Theoretical Computer Science* 74(3), 253–271 (1990), DOI `10.1016/0304-3975(90)90077-U` |

A chapter titled **"Successive Difference Substitution"** (DOI `10.1142/9789814759120_0010`)
appears in the bibliographic search for the 2016 book. **Only the chapter title and DOI were
obtained; the chapter was not read.** Nothing in this registration depends on its contents,
and no completeness, convergence or complexity claim about the method is made here.

## 3. Not retrieved

- The Baidu entry for Yang Lu named in the request ("百度安全验证").
- The Chinese Wikipedia entries for either mathematician.
- Every full text: the 2003 journal paper, the 1988 and 1990 papers, and the 2016 book
  including its successive-difference-substitution chapter.
- Any source for the cohort framing "Peking University mathematics' first golden
  generation"; only the shared 1959 graduation is established above.

## 4. Relation to this repository's own run

`docs/research/0185-yang-difference-substitution-inequalities.md` and
`experiments/yang_sds_inequalities/` test a sound subset of the difference-substitution idea
on eight polynomial inequalities, with their own frozen contract, checker and residual. That
run is **not** evidence for anything here, and this registration is not authority for it:
the run cites section 2 for what the sources say and answers for its own measurements
itself. In particular the run's certificate is its own construction, and its `Unknown`
outcomes are not a statement about the published program.

## 5. Open obligations

- No checker, no evidence file and no executed run: this entry introduces no executable
  claim and changes nothing in `docs/claims.toml`.
- The method's name, program, reach and benchmark rest on one journal abstract; the
  algorithm itself was not read, so the relation between that method and any
  difference-substitution certificate remains unestablished here.
- The claim that the program can disprove as well as prove is quoted and not tested.
- The awards and positions are quoted from the institute page and were not independently
  confirmed.
- Nothing was verified about the method's complexity or the efficiency claim in the
  abstract.

## 6. Explicit non-claims

- This is a documentary registration, not a derivation parent, not a Pascal descendant, not
  a growth-obligation successor, and not a semantic authority.
- It grants no native admission, no Seal and no geometry catalog successor; the
  Pascal-rooted growth obligation stays Open.
- It does not claim that any inequality method is correct, complete or applicable to
  statements outside those this repository runs.
- No priority, historical completeness or bibliographic completeness is claimed, and the
  cohort framing quoted in section 1 is not endorsed.
