# 六条直线，不是六个点：Calabi–Yau 五十年的学习笔记（层 v1）

English abstract: An appending layer to the Calabi–Yau fifty-years study note. It
adds two source groups to the note's bibliography and records one distinction
that must not be collapsed: the real "six → Calabi–Yau" literature in the
projective plane runs on **six lines**, not on six points on a conic. It rewrites
nothing in v0, keeps the v0 pin valid, and makes no new mathematical claim. It
also records the searches that returned nothing, so that the absence of a
Pascal-to-Calabi–Yau bridge is stated as a search result and not as a theorem.

日期：2026-09-22。版本：v1（追加层）。目录身份与 v0 相同：`proposed-document`，
几何目录的 `external-reference`，条目键 `geometry-calabi-yau-fifty-years-reading`。

本层**追加**于
[`yau-calabi-yau-fifty-years-reading-note-v0.md`](yau-calabi-yau-fifty-years-reading-note-v0.md)，
**不改写它**，v0 的字节 pin 继续有效。v0 仍是那次阅读与首次整理的记录，包括
本层补充或更正的部分。与 v0 一样，本层**不是**推导父项、**不是**语义权威、
**不是** claim、**不是**证据；没有检查器、没有运行、没有数学准入。

撰写、资料核对与仓库整合：deepseek-v4-flash-vision-exp（DeepSeek Harness），
经 Mingli Yuan 的授权账号代理提交；他未审阅、未背书。原创贡献按
[Unknown v0.3](Unknown-LICENSE-v0.3.md) 提供。

---

## 0. 为什么有这一层

2026-09-22，苑明理提出一个几何直觉并要求查文献（原话）：

> 六维泰西穆勒空间上三孔算术表达式计算机两个共轭互联，切开后共有 6 孔，这 6 孔
> 我直觉和 Pascal 定理有关系，在 Pascal 定理这个关系是一个圆。在 6 维空间两个
> 共轭互联的算术表达式计算机应该呈现为 Calabi-Yau 流形。我想请你帮我查找一下，
> 有没有 Calabi-Yau 切开一个圆得到 6 孔的研究文献

检索的结论分两半，且**两半的方向相反**：

- 「Calabi–Yau 沿一个圆切开得到 6 个孔」——**没有这个文献**，并且被一个拓扑
  事实挡住（见第 3 节）。
- 「六个某物 → Calabi–Yau」——**有真文献，而且很热**；但那个「某物」是
  **$\mathbb P^2$ 中的六条直线**，不是**圆锥曲线上的六个点**。

本层把后者的两条来源编入 v0 第 8 节的文献组（本层编号 **R24、R25**），并把
必须写明的区别写在第 2 节。**v0 第 8 节的 R1–R23 编号与内容一字不动。**

## 1. 新增文献（本层编号 R24、R25）

| 编号 | 文献 | 核对范围 |
| --- | --- | --- |
| <a id="r24"></a>R24 | Hosono–Lian–Takagi–Yau，[K3 surfaces from configurations of six lines in $\mathbb P^2$ and mirror symmetry I](https://arxiv.org/abs/1810.00606) | arXiv 记录页的标题、作者、日期与摘要（2026-09-22 取回）；**未读全文** |
| <a id="r25"></a>R25 | Clingher–Malmendier–Shaska，[Six line configurations and string dualities](https://arxiv.org/abs/1806.07460) | 同上 |

核对深度**只到摘要与书目**，不表示逐页通读，也不表示本仓库复核过其中任何
证明。源文件没有随笔记入库。

### 1.1 R24 说了什么

摘要原文（英）：

> From the viewpoint of mirror symmetry, we revisit the hypergeometric system
> $E(3,6)$ for a family of K3 surfaces. We construct a good resolution of the
> Baily–Borel–Satake compactification of its parameter space, which admits
> special boundary points (LCSLs) given by normal crossing divisors. We find
> local isomorphisms between the $E(3,6)$ systems and the associated GKZ systems
> defined locally on the parameter space and cover the entire parameter space.
> Parallel structures are conjectured in general for hypergeometric system
> $E(n,m)$ on Grassmannians. Local solutions and mirror symmetry will be
> described in a companion paper, where we introduce a K3 analogue of the
> elliptic lambda function in terms of genus two theta functions.

中文要点：从镜像对称的角度重访 K3 曲面族的**超几何系统 $E(3,6)$**；构造其参数
空间 Baily–Borel–Satake 紧化的**好解消**，其上有由正规交叉除子给出的特殊边界点
（LCSL）；在参数空间局部把 $E(3,6)$ 系统与相应 GKZ 系统同构并覆盖全空间；对
Grassmannian 上的 $E(n,m)$ 猜想有并行结构；companion paper 用**亏格 2 theta
函数**给出 K3 版的椭圆 lambda 函数。

**作者含 Yau。** 与 v0 第 8 节已有的 R13（Lian–Liu–Yau，*Mirror Principle I*）
同域，因此本层把它编入同一文献组而不是另立条目。

### 1.2 R25 说了什么

摘要原文（英）：

> We study the family of K3 surfaces of Picard rank sixteen associated with the
> double cover of the projective plane branched along the union of six lines,
> and the family of its Van Geemen–Sarti partners, i.e., K3 surfaces with
> special Nikulin involutions, such that quotienting by the involution and
> blowing up recovers the former. We prove that the family of Van Geemen–Sarti
> partners is a four-parameter family of K3 surfaces with
> $H\oplus E_7(-1)\oplus E_7(-1)$ lattice polarization. We describe explicit
> Weierstrass models on both families using even modular forms on the bounded
> symmetric domain of type IV. We also show that our construction provides a
> geometric interpretation, called geometric two-isogeny, for the F-theory /
> heterotic string duality in eight dimensions. As a result, we obtain novel
> F-theory models, dual to non-geometric heterotic string compactifications in
> eight dimensions with two non-vanishing Wilson line parameters.

中文要点：**沿六条直线之并的 $\mathbb P^2$ 二重覆盖**所给出的 Picard 秩 16 的
K3 曲面族，及其 Van Geemen–Sarti 伴侣族（带特殊 Nikulin 对合）；伴侣族是
$H\oplus E_7(-1)\oplus E_7(-1)$ 极化的四参数族；用 IV 型有界对称域上的偶模形式
写出两族的显式 Weierstrass 模型；该构造给出 **F-理论／杂弦八维对偶**的几何解释
（名为 geometric two-isogeny），并得到对偶于八维非几何杂弦紧化的新 F-理论模型。

## 2. 必须写明的区别：六条直线，不是六个点

本条是本层存在的理由，也是任何引用 R24／R25 时必须同时写出的一句：

| | 对象 | 结果 |
| --- | --- | --- |
| Pascal 定理 ／ hexagrammum mysticum | 圆锥曲线上的**六个点**，$60$ 条 Pascal 线 | 古典射影几何；由 $S_6$ 的外自同构组织 |
| R24 ／ R25 | $\mathbb P^2$ 中的**六条直线** | K3 曲面（Picard 秩 16 或 20）、F-理论／杂弦对偶、镜像对称 |

**这两者不是同一件事，也不互相推出。** 把 R24／R25 记成「Pascal 的六个点」是
张冠李戴；反过来，用它们支持任何关于 Pascal 的陈述也没有依据。

本笔记 v0 从未讨论 Pascal。本层**也不建立** Pascal 与 Calabi–Yau 的联系。

### 2.1 检索到的「无」同样要记

以下「0 命中」是本层撰写时实际执行并读到的结果。**「某查询返回 0」不等于
「文献不存在」**，只等于该查询没有命中：

| 查询 | 命中 |
| --- | ---: |
| arXiv `abs:"six holes"` | 8 条，全部凝聚态／光纤／量子点噪声，**数学类 0** |
| arXiv `abs:"three holes" AND abs:"Teichmuller"` | **0** |
| arXiv `abs:"circle fibration" AND abs:"K3"` | **0** |
| arXiv `abs:"Teichmuller" AND abs:"Calabi-Yau"` | 2 条（其一即本笔记已引的 Liu–Sun–Yau 2009） |

另有一组**元数据**检索（OpenAlex／arXiv 标题与摘要）报告为 0：`"Pascal's
theorem" AND "Calabi-Yau"`、`"Pascal lines" AND "K3"`、`"Pascal hexagrammum
Calabi-Yau"`，以及 arXiv `hexagrammum` 恰 4 条且无一涉及 Calabi–Yau。**这四条
本层未独立复核，按转述记录。**

**因此本层不作任何「Pascal ↔ Calabi–Yau 存在桥」的陈述**，无论正向还是反向。

## 3. 与「6」有关的结构事实

以下为**标准事实**，本层未取回专门引文，按标准事实陈述：

1. 单连通的 Calabi–Yau 三fold 有 $b_1=0$，即**没有非平凡圆类**。所以「沿一个
   圆切开一个 Calabi–Yau」在拓扑上不是一个有定义的操作。
2. Calabi–Yau 的计数用 Hodge 数 $h^{1,1}$、$h^{2,1}$（$\chi=2(h^{1,1}-h^{2,1})$）
   与 Betti 数（$b_2=h^{1,1}$，$b_3=2(1+h^{2,1})$）；**「一个有 6 个孔的
   Calabi–Yau」在标准用法里没有定义**。文献中 Calabi–Yau 语境下的 "holes" 已
   被占用为别的东西（有效锥中没有整体截面的除子类）。
3. **「6 个独立圆类」的对象是六维环面 $T^6$**，按宽泛的 $c_1=0$ 约定可称
   Calabi–Yau，但**不是**不可约 $SU(3)$ 和乐的三fold。**本仓
   `adva/docs/research/0043-scale-marked-surface-exploration.md` §2 已经就
   $E_{\lambda_0}\times E_{\lambda_1}\times E_{\lambda_2}$ 判定过同一件事**，
   并同时写明「$H^3$（参数域）与每个 $X_\lambda$（纤维）实维数都是 6，但两者
   不是同一个对象」。

**结论**：六实维正确地指向 Calabi–Yau 三fold；但那个「6」是**维数**，不是孔数。
本层不认为 `meaning-interpretation-v0.md` §1 的「6 维泰西穆勒结构」与 Calabi–Yau
之间存在已建立的等同，也不认为本层能提供这样的等同。

## 4. 本层不改变什么

- **v0 的字节与 pin 不动。** v0 第 8 节的 R1–R23 编号、内容与表格一字不改；
  R24、R25 是**本层**的编号。
- 本层与 v0 **共用同一个目录学条目键** `geometry-calabi-yau-fifty-years-reading`；
  本层作为该条目的第二份 material 登记，不新增条目，不改变 `math/README.md`
  的条目计数（33 条）与主题计数（$10/10/18$）。
- 不改 `docs/claims.toml`；**无原生准入**；无新的几何增长结论；Pascal 根增长
  义务仍为 `Open`，native `Seal` 仍为 `NotIssued`。
- **不建立** Q4/M6 与 Teichmüller 空间的等同（`MT1` 对此仍未证明），也不建立
  与 Calabi–Yau 的等同。
- 本层不是任何实验的契约、检查器或证据。

## 5. 收录与使用边界

本层的中文说明、问题组织、区别陈述、检索记录与登记元数据是此次新写的贡献。
数学定义、公式与书目信息用于说明公开的数学事实；**第三条的来源只以书目标识与
链接定位**，其正文、插图与版式未纳入发布单元。外部链接仅定位来源，不赋予其目标
任何新许可。本层的发表审查见
[准入记录](governance/publication/records/calabi-yau-fifty-years-reading-v1-2026-09-22.json)；
该记录是撰写方的发布内容审查，**不是**独立数学评审。

v0 的准入记录
（[`calabi-yau-fifty-years-reading-2026-09-20.json`](governance/publication/records/calabi-yau-fifty-years-reading-2026-09-20.json)）
继续是 **v0 字节**的记录，本层不改写它。

目录检查只检验结构、归属与字节指纹，**不检验本层任何陈述为真**。本层所述「无
文献」一律是查询结果，不是不存在性的证明；所述标准事实未附专门引文者已逐条
注明。任何后续可执行研究都须另定问题、输入条件、检查器与有限资源范围。
