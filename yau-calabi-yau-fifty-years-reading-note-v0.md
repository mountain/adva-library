# 从典范度量到镜像对称：Calabi–Yau 五十年的学习笔记

English abstract: An original Chinese study note on canonical metrics, stability,
mirror symmetry and higher-genus curve counting, prompted by a supplied memoir of
Shing-Tung Yau. It distinguishes published theorems, conjectural correspondences,
physical motivations and arithmetic expectations. Sources are cited by links;
their prose, the memoir, its poem and illustrations are not reproduced.

日期：2026-09-20。版本：v0。目录身份：`proposed-document`，几何目录的
`external-reference`；条目键为 `geometry-calabi-yau-fifty-years-reading`。
阅读任务与收录方向：Mingli Yuan。撰写、资料核对及仓库整合：Codex（OpenAI），
通过 Mingli Yuan 的授权账号代理提交；账号使用不表示其亲自撰写、评审或担保。
原创贡献按 [Unknown v0.3](Unknown-LICENSE-v0.3.md) 提供。

这篇笔记以用户提供的《Calabi-Yau 流形五十年，我的回忆》中文文本为阅读起点，
按数学问题重新组织本次讨论。它是独立讲解，不是原文转载、逐段翻译或证明论文。
回忆文字的正式版本与发表信息尚未核实；下文的技术结论分别指向主要文献。
文献核对覆盖书目信息、摘要及有关选段，没有逐篇通读或独立复核全部证明。

我们关心三个相互联系的问题：给定复几何与拓扑条件，怎样找到典范度量；
两种看起来不同的几何，怎样通过镜像发生联系；无限多个曲线计数，怎样组织成
受有限代数结构约束的函数。稳定性贯穿前两个问题，周期与生成函数连接后两个问题。

## 1. 用一个函数寻找一个度量

无物质、宇宙学常数为零时，在维数大于二的背景中，Einstein 真空方程等价于
$\operatorname{Ric}(g)=0$。广义相对论使用 Lorentz 度规；几何分析可以先在
正定的 Riemann 度规中研究这个方程。两者共享曲率表达式，但正定解本身并不自动
给出物理时空。紧致 Riemann 流形自动完备，因而紧致情形提供了清楚的研究起点。

Ricci 张量是完整曲率张量的一种收缩。令 Ricci 曲率消失，仍然允许完整曲率非零。
因此，“Ricci 平坦”与“局部欧氏”是不同条件；K3 曲面上的 Ricci 平坦度量是重要例子。
回忆中关于早期已知例子的说法，应按作者当时的研究处境理解，不扩写成没有条件的
数学史断言。

Kähler 几何使这个问题出现特别简洁的形式。局部写度量为 $g_{j\bar k}$，其
Ricci 形式为

$$
\rho(\omega)=-i\partial\bar\partial\log\det(g_{j\bar k}),
\qquad [\rho(\omega)]=2\pi c_1(X).
$$

这里不随度量变化的是右侧的上同调类；具体微分形式 $\rho(\omega)$ 会变化。
行列式又决定体积形式，于是控制体积成为控制 Ricci 曲率的途径。

在固定的连通紧致 Kähler 流形与 Kähler 类上，另一个同类 Kähler 形式可写成

$$
\omega_\varphi=\omega_0+i\partial\bar\partial\varphi>0.
$$

指定体积形式就得到复 Monge–Ampère 方程

$$
(\omega_0+i\partial\bar\partial\varphi)^n=e^f\omega_0^n,
\qquad
\int_X e^f\omega_0^n=\int_X\omega_0^n.
$$

未知量只有一个实函数 $\varphi$，其二阶导数却决定整个度量的改变。
正定性条件给出椭圆性。若 $c_1(X)=0\in H^2(X,\mathbb R)$，可以选择满足
$i\partial\bar\partial f=\rho(\omega_0)$ 的归一化函数，所求度量便有零 Ricci 曲率。
Yau 的存在性定理与 Calabi 的唯一性结论合起来说明：**固定复结构和 Kähler 类后，
存在唯一的 Ricci 平坦 Kähler 度量**。[R1](#r1)、[R2](#r2)

这里使用了紧致 Kähler 结构，并非只输入一个任意拓扑空间便能得到度量。
若 Kähler 类来自 ample 线丛，则进一步得到通常意义上的极化资料；任意实
Kähler 类不能直接等同于这样的代数极化。

证明的难点是先验估计。连续性方法需要控制势函数、度量及更高导数，阻止求解过程中
发生失控或退化。1976 年的突破与随后发表的完整证明，应放在这个分析框架中理解。
诗序把多年研究和个人生活连接起来，具有回忆的价值；它不替代估计本身。
2014 年的落款属于诗及其注释，不足以确定整篇回忆中相对年代的基准。
Calabi 猜想的证明归于丘成桐；与郑绍远、Schoen、Simon 等共同发展几何分析的历程，
则是更广的合作背景。[R1](#r1)

## 2. 典范度量怎样产生几何信息

唯一性赋予度量一种用途：固定复结构和 Kähler 类后，长度、体积、算子谱等量不再
依赖另行任意挑选的背景度量。它们因此成为研究这组几何资料的自然不变量。

例如，标量 Laplace 算子的特征函数满足 $\Delta_g f_j=\lambda_j f_j$。
特征值、节点集与水平集反映全局几何，可用来研究分区与空间结构。这个观点并不保证
每个水平集都给出唯一的典范分区：重特征值允许在特征空间中重新选基，实特征函数
也有符号选择。Dirac 谱同样重要，但须固定相应旋量结构，其特征对象通常是旋量，
不能直接当作普通标量函数。一个算子的谱也没有普遍的“唯一恢复全部复几何”保证。

另一条路径是 Chern–Weil 理论：用曲率表达 Chern 类，再利用特殊度量把曲率的正性
转换成代数几何中的数值限制。以典范丛 ample 的光滑紧致复曲面为例，负曲率
Kähler–Einstein 度量给出

$$
c_1^2(X)\le 3c_2(X).
$$

在这些条件下，等号对应复球的商。这是 Miyaoka–Yau 不等式及其等号几何的重要情形。
此处已经从零第一 Chern 类进入负第一 Chern 类的情形：同一种分析方法服务于更广的
代数几何问题。几何分析的作用由此变得具体——解方程之后，可以得到拓扑数值的限制，
甚至识别达到极值的空间。[R3](#r3)

## 3. 稳定性控制存在性

局部写下一个椭圆方程，不能保证它在给定的整体对象上可解。退化方向、对称性和能量
行为可能形成障碍。文中所说的非紧致性可以属于变换群；底流形仍然可以紧致。
稳定性的一个核心用途，是以代数或几何条件识别这种整体障碍。

对紧致 Kähler 流形上的全纯向量丛 $E$，Hermitian–Yang–Mills 方程可写成

$$
F_A^{0,2}=0,\qquad i\Lambda_\omega F_A=\lambda\operatorname{Id}_E.
$$

第一条与全纯结构相容，第二条约束曲率的平均部分。
Donaldson–Uhlenbeck–Yau 对应把解的存在性与斜率多重稳定性联系起来。
斜率的基本形式是

$$
\mu_\omega(E)=\frac{1}{\operatorname{rk}E}
\int_X c_1(E)\wedge\omega^{n-1}.
$$

稳定性检验所有适当的非零真相干子层的斜率；多重稳定允许同斜率稳定因子的直和。
因而完整的存在性对应应保留“多重稳定”这一条件。矩映射观点把曲率方程解释为
取指定矩映射值的问题，并把稳定性与复化群轨道的行为联系起来。[R4](#r4)

Simpson 把这一结构推进到 Higgs 丛 $(E,\theta)$，其中
$\theta:E\to E\otimes\Omega_X^1$，且 $\theta\wedge\theta=0$。
检验稳定性时，要考察被 $\theta$ 保持的子对象。在适当的陈类消失条件下，
多重稳定 Higgs 丛与半单局部系统相对应，从而联系基本群表示与全纯几何。
Hodge 结构的变分处在这个更广的非阿贝尔 Hodge 理论中。[R5](#r5)

度量问题也有相似结构，但不同对象的稳定性定义不能互换。
光滑 Fano 流形的 Kähler–Einstein 度量存在性与 K-多重稳定性对应；这里的稳定性
通过代数退化及其不变量刻画，不是把向量丛斜率原封不动搬过来。[R6](#r6)

至于同调类稳定性与 Hodge 猜想，回忆表达的是研究方向。对光滑射影复流形，
有理 Hodge 猜想要求每个有理 $(p,p)$ 类成为代数循环类的有理线性组合；
Poincaré 对偶允许改用同调语言。尚不能把某个已经确定的稳定性条件与 Hodge 猜想
写成已证等价关系。[R7](#r7)

## 4. 从弦论动机到可检验的曲线计数

1984 年的第一次弦论革命是背景；Candelas、Horowitz、Strominger、Witten 的经典
紧化论文发表于 1985 年。在其适当的超对称、通量和近似条件下，十维背景可以考虑为
四维时空与六实维内部空间的乘积。Calabi–Yau 三维簇提供了重要的内部几何。
一个完整真空还包含规范丛和其他场数据；这是一类候选模型，并非对现实内部空间的
实验识别。[R8](#r8)

欧拉示性数 $\pm6$ 的要求有明确但有限定的物理来源。在相关异质弦标准嵌入模型中，
净手征代数的绝对值是 $|\chi(X)|/2$，所以三代的净指数引出 $|\chi|=6$。
它并不确定全部粒子谱，也不是任意紧化模型都满足的无条件公式。
在 $h^{1,0}=h^{2,0}=0$、$h^{3,0}=1$ 的紧致 Calabi–Yau 三维情形，有

$$
\chi(X)=2\bigl(h^{1,1}(X)-h^{2,1}(X)\bigr).
$$

Yau 的一项构造从 $\mathbb P^3\times\mathbb P^3$ 中多次数分别为
$(3,0),(0,3),(1,1)$ 的光滑完全交出发，其欧拉示性数为 $-18$；
选择自由的 $\mathbb Z_3$ 作用后，商空间的欧拉示性数为 $-6$。
这里采用自由商，不能与镜像构造中需要处理奇点的商混淆。[R9](#r9)

Greene–Plesser 提供的镜像证据把复结构模与复化 Kähler 模联系起来。
在三维情形，镜像交换 $h^{1,1}$ 与 $h^{2,1}$，因而改变欧拉示性数的符号。
五次三维簇与其镜像的 Hodge 数分别为 $(1,101)$ 与 $(101,1)$。
这些数值交换是重要检验，但数值符合本身不足以定义完整的镜像关系。[R10](#r10)

下一步是 Candelas、de la Ossa、Paul Green 和 Parkes 的曲线计数计算。
Paul Green 与前文的 Brian Greene 是不同的人。对五次三维簇，镜像一侧的全纯三形式
周期满足 Picard–Fuchs 微分方程；经过镜像映射，它们产生原流形的亏格零计数资料。
用通常的归一化表示，Yukawa 耦合展开为

$$
K(q)=5+\sum_{d\ge1}n_d\,d^3\frac{q^d}{1-q^d},
\qquad
n_1=2875,\quad n_2=609250,\quad n_3=317206375.
$$

其中 $q$ 记录曲线次数；$n_d$ 是按多重覆盖关系组织的计数，不能对所有次数都
未经论证地当作光滑嵌入曲线的朴素个数。$2875$ 是一般光滑五次三维簇上的直线数。
严格数学框架使用稳定映射与 Gromov–Witten 不变量。[R11](#r11)、[R12](#r12)

Givental 和连文豪、刘克峰、丘成桐的工作为相应镜像公式提供了严格证明。
这里证明的是指定范围内的枚举镜像公式，并不等于证明所有版本的镜像对称。
这也补上了阅读时的重要连接：镜像关系首先带来亏格零的精确计算，随后才进入
高亏格的 BCOV 理论。[R12](#r12)、[R13](#r13)

## 5. 镜像的两种解释及其稳定性问题

Kontsevich 的同调镜像对称把对应提升到范畴层面。示意地写为

$$
D^\pi\operatorname{Fuk}(X)\simeq D^b\operatorname{Coh}(\check X).
$$

左侧以带适当附加资料的 Lagrangian 对象、Floer 理论和全纯多边形为基础；
右侧由凝聚层及其复形组成。真正的陈述需要指定范畴增强、系数和完成方式。
它试图对应对象及其态射、组合等结构，远超出 Hodge 数相等。[R14](#r14)

Strominger–Yau–Zaslow 的思路则从空间的纤维结构出发。在适当情形及极限中，
考虑特殊 Lagrangian 环面纤维化；在光滑部分，以对偶环面替换每个纤维。
对三维 Calabi–Yau，纤维是三实维环面，底也是三实维。纤维 $L$ 的对偶环面可写为

$$
\operatorname{Hom}(H_1(L,\mathbb Z),U(1)),
$$

即平坦 $U(1)$ 线丛的模空间。因而镜像一侧的点，自然对应原空间的一个环面纤维
及其平坦联络。这与同调镜像中的点层提供了接点。整体构造还必须处理奇异纤维和
瞬子修正；逐纤维取对偶只是平滑、半平坦部分的起点。[R15](#r15)

这里的特殊 Lagrangian 讨论要求全局非消失的全纯体积形式；这比仅要求实第一
Chern 类为零增加了资料。在带 Kähler 形式 $\omega$ 和归一化全纯体积形式 $\Omega$ 的 Calabi–Yau 上，
实 $n$ 维子流形 $L$ 满足 $\omega|_L=0$ 时称为 Lagrangian；再满足

$$
\operatorname{Im}(e^{-i\theta}\Omega)|_L=0,
\qquad
\operatorname{Re}(e^{-i\theta}\Omega)|_L=\mathrm{vol}_L
$$

且 $\theta$ 为常数时，称为特殊 Lagrangian。第二个条件保留取向与正分支。
“cycle”在此应按几何或同调循环理解，并不意味着一维圆，也不要求总是环面。

Thomas–Yau 猜想把相应稳定性与 Hamiltonian 类中的特殊 Lagrangian 代表联系起来。
Hamiltonian 形变比任意连续形变或仅保持同调类更强。周期
$Z(L)=\int_L\Omega$ 及其相位提示了稳定性的结构，但只比较一个对象自己的相位
不足以定义稳定性，还要控制适当的子对象或分解。[R16](#r16)

Lagrangian 平均曲率流提供了寻找代表的分析思路。奇点、手术、分级及允许的对象类别
使精确陈述十分重要；应结合后来的修正理解，不能断言任意“稳定”光滑循环都会
无奇点地流到特殊 Lagrangian。[R17](#r17)

Leung–Yau–Zaslow 在半平坦镜像模型中研究特殊 Lagrangian 的对应物。
对适当的截面及平坦局部系统，镜像可成为全纯线丛；特殊性转化为变形
Hermitian–Yang–Mills（dHYM）方程。秩一情形，把规范化常数吸收到实曲率形式
$\alpha$ 后，可写成

$$
\operatorname{Im}\!\left(e^{-i\hat\theta}(\omega+i\alpha)^n\right)=0,
\qquad
\operatorname{Re}\!\left(e^{-i\hat\theta}(\omega+i\alpha)^n\right)>0.
$$

令 $\lambda_j$ 为 $\omega^{-1}\alpha$ 的特征值，局部相位表达式是 $\sum_j\arctan\lambda_j=\hat\theta$，并须选择适当的相位提升。
对平坦模型中的图 $L_u=\{x+i\nabla u(x)\}$，拉回体积形式出现
$\det(I+iD^2u)$，这解释了 Monge–Ampère 型结构从何而来。
一般的特殊 Lagrangian 并不都在全局上对应普通向量丛，秩一方程也不自动覆盖高秩问题。
[R18](#r18)

回忆中文本的“Adams”，结合有关论文的作者名单，应核对为 **Adam Jacob**。
Collins、Jacob、Yau 的工作研究相位方程的先验估计、次解条件及代数障碍；例如超临界
相位范围中有重要存在性结果。这些条件是定理的一部分，不能省略为任意丛上的普遍
可解性。[R19](#r19)

## 6. 高亏格生成函数与有限代数结构

BCOV 理论来自 Bershadsky、Cecotti、Ooguri、Vafa，研究 B 模型中的
Kodaira–Spencer 引力及高亏格振幅，并通过镜像联系 A 模型曲线计数。
亏格 $g$ 对光滑紧致曲线表示其拓扑把手数；$g=0$ 对应球面，$g=1$ 对应环面。
以单参数模型为例，用 $N_{g,d}$ 表示适当的亏格 $g$、次数 $d$ 的
Gromov–Witten 不变量，生成函数示意为

$$
F_g(q)=\sum_{d\ge0}N_{g,d}q^d,
\qquad
Z=\exp\!\left(\sum_{g\ge0}g_s^{2g-2}F_g\right).
$$

$g_s$ 是组织亏格展开的参数。低亏格还需处理经典项等约定；$F_g$ 通常称自由能
或振幅，总配分函数则是 $Z$。这里计数的是稳定映射的虚拟贡献，允许退化和
多重覆盖，不是清点所有光滑曲线后得到的整数序列。[R20](#r20)

BCOV 的全纯反常方程把高亏格振幅的反全纯依赖与低亏格资料联系起来。
其几何图景来自曲线退化：可以捏缩一个非分离环而降低亏格，也可以分裂成两个
较低亏格的分支。递推仍留下全纯歧义，需要边界条件等额外资料固定。
因此它提供强大的计算结构，但不独自确定所有答案。[R20](#r20)

Yamaguchi–Yau 对五次三维簇等研究对象发现了特别紧凑的多项式结构。
在相应坐标与归一化下，亏格 $g\ge2$ 的振幅可写成五个生成元的多项式；
常用记号是 $V_1,V_2,V_3,W_1,Y_1$，权重分别为 $1,2,3,1,1$，
总加权次数为 $3g-3$。这把无限多个亏格的函数放入同一个有限生成的环境环中。
它不意味着已经算出所有多项式的系数，全纯歧义仍须处理。[R21](#r21)

还有一个容易忽略的代数区别。即使每个 $F_g$ 都属于有限生成的函数环
$R$，也不能仅凭包含关系断言子代数 $\mathbb C[F_2,F_3,\ldots]$
有限生成。一个初等例子是

$$
A=\mathbb C[x,xy,xy^2,xy^3,\ldots]\subset\mathbb C[x,y].
$$

右侧由两个元生成，左侧却不能由有限个元生成：任何两个非常数单项式相乘，
$x$ 次数至少是二；所以要生成所有 $x$ 次数恰为一的 $xy^k$，
有限生成元的一次部分必须张成一个无限维向量空间，这是不可能的。
这个例子只解释包含关系的逻辑限制，不是对 BCOV 函数之间实际关系的反例。

Guo、Janda、Ruan 后来从五次三维簇的 A 模型出发，证明了相应的有限生成、
全纯反常及 orbifold 正则性结果。必须读取具体定义与范围，不能将其理解为
全部 Calabi–Yau、所有边界条件和所有高亏格计算均已完成。[R22](#r22)

数论类比由椭圆曲线提供。对 $SL_2(\mathbb Z)$，全纯模形式环由
$E_4,E_6$ 生成，拟模形式环由 $E_2,E_4,E_6$ 生成；无穷多个函数因此受
少数基本函数及其关系控制。椭圆曲线的周期、模参数和算术结构又紧密联系。
Calabi–Yau 的周期、镜像映射及高亏格生成函数提示了高维类似结构的可能性。
但有限生成性本身既不证明这些函数是经典模形式，也不证明其系数的整性或完整的
算术对应。这里保留的是有具体结构支持的研究愿景。[R23](#r23)

## 7. 阅读时保留的结论层次

| 内容 | 本笔记采用的身份与限制 |
| --- | --- |
| Calabi–Yau 度量存在唯一性 | 紧致 Kähler、实第一 Chern 类为零；固定复结构与 Kähler 类 |
| 丛的 HYM 存在性 | 在相应背景下，与斜率多重稳定性对应 |
| Fano 的 Kähler–Einstein 存在性 | 与 K-多重稳定性对应，稳定性定义不同于丛斜率 |
| Hodge 猜想与循环稳定性 | 研究设想，未给出一般已证等价关系 |
| 欧拉示性数 ±6 与三代 | 指定异质弦标准嵌入中的净指数动机 |
| Candelas 公式 | 相应亏格零镜像公式已有严格证明，具体范围见原论文 |
| 同调镜像与 SYZ | 广泛的研究框架；各模型的已知结果须分别查证 |
| Thomas–Yau | 有对象条件及后续修正的猜想框架 |
| dHYM | 有相位、次解等假设的分析结果及代数障碍 |
| Yamaguchi–Yau 与后续五次簇结果 | 指定模型和归一化下的代数结构；不等于所有系数已知 |
| Calabi–Yau 在数论中的作用 | 已有具体联系支持的进一步研究方向 |

本文补足了前期逐段阅读中没有展开的 Candelas 枚举公式、Chern 数应用、谱的限制及
Higgs 丛线索。它覆盖所供全文的主要数学主题，并未逐一考证人物生平、题图信息、
诗词训诂或研究热度的历史判断。“大约十五年前”等相对年代保留为待核对信息。

已有的 [Yau–Calabi 算术映射笔记](meaning-yau-calabi-mapping-v0.md) 是另一种用途的
历史类比提案。本篇不由那些有限算术收据推出 Calabi–Yau 定理，也不把矩阵谱互逆
识别成镜像对称。旧笔记中把 Ricci 形式直接写成拓扑不变量的简写，应按本文第 1 节
区分形式和上同调类；这里公开记录校正，保留旧记录的原始字节。

## 8. 主要文献与本次阅读深度

下表只保存书目与外部链接。标注“选段”表示核对了与本文结论相关的正文或公式，
不表示逐页通读；“摘要”不能作为复核技术证明的替代。源文件没有随笔记入库。

| 编号 | 文献 | 核对范围 |
| --- | --- | --- |
| <a id="r1"></a>R1 | Yau，1978，[On the Ricci curvature of a compact Kähler manifold and the complex Monge–Ampère equation, I](https://doi.org/10.1002/cpa.3160310304) | 期刊书目；存在性叙述另与 R2 对照 |
| <a id="r2"></a>R2 | Calabi / LeBrun，[Simons Center 访谈](https://scgp.stonybrook.edu/archives/31629) | 指定体积、存在性与唯一性的访谈选段 |
| <a id="r3"></a>R3 | Yau，[The Role of Partial Differential Equations in Differential Geometry](https://archive.ymsc.tsinghua.edu.cn/pacm_download/59/11114-Shing-Tung_Yau_217.pdf) | ICM 报告中陈数不等式及球商选段 |
| <a id="r4"></a>R4 | Uhlenbeck–Yau，1986，[On the existence of Hermitian–Yang–Mills connections in stable vector bundles](https://doi.org/10.1002/cpa.3160390714)；[Donaldson 关于 Kähler 几何的讲义](https://www.claymath.org/wp-content/uploads/2022/03/Donaldson-AG2015.pdf) | 原论文书目、讲义相关陈述；未复核证明 |
| <a id="r5"></a>R5 | Simpson，1992，[Higgs bundles and local systems](https://www.numdam.org/item/PMIHES_1992__75__5_0/) | 书目及可访问的定义、对应关系选段 |
| <a id="r6"></a>R6 | Chen–Donaldson–Sun，[Kähler–Einstein metrics on Fano manifolds, III](https://arxiv.org/abs/1302.0282) | 摘要及 R4 讲义的稳定性叙述 |
| <a id="r7"></a>R7 | Deligne，[The Hodge Conjecture](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf) | 猜想陈述及适用对象 |
| <a id="r8"></a>R8 | Candelas–Horowitz–Strominger–Witten，1985，[Vacuum configurations for superstrings](https://ooguri.caltech.edu/documents/31340/Candelas_Horowitz_Strominger_Witten.pdf) | 紧化背景、假设及书目选段 |
| <a id="r9"></a>R9 | Yau，2006，[Spacetime and the Geometry behind it](https://archive.ymsc.tsinghua.edu.cn/pacm_download/59/11285-Shing-Tung_Yau_816.pdf) | 构造、欧拉示性数及镜像史相关选段 |
| <a id="r10"></a>R10 | Greene–Plesser，[Mirror Manifolds: A Brief Review and Progress Report](https://arxiv.org/abs/hep-th/9110014) | 镜像商构造与 Hodge 数相关选段 |
| <a id="r11"></a>R11 | Candelas–de la Ossa–Green–Parkes，1991，[A pair of Calabi–Yau manifolds as an exactly soluble superconformal theory](https://www.staff.science.uu.nl/~beuke106/HypergeometricFunctions/COGP.pdf) | 摘要、书目；枚举公式另与 R12 对照 |
| <a id="r12"></a>R12 | Givental，[Equivariant Gromov–Witten Invariants](https://math.berkeley.edu/~giventh/papers/eqv.pdf) | 开篇定理、周期变换、计数公式及多重覆盖说明 |
| <a id="r13"></a>R13 | Lian–Liu–Yau，[Mirror Principle I](https://arxiv.org/abs/alg-geom/9712011) | 摘要及证明范围 |
| <a id="r14"></a>R14 | Kontsevich，[Homological Algebra of Mirror Symmetry](https://arxiv.org/abs/alg-geom/9411018) | 范畴对应的相关选段 |
| <a id="r15"></a>R15 | Strominger–Yau–Zaslow，[Mirror Symmetry is T-Duality](https://arxiv.org/abs/hep-th/9606040)；Gross，[Mirror Symmetry and the Strominger–Yau–Zaslow conjecture](https://arxiv.org/abs/1212.4220) | 环面纤维、局部系统及奇异修正的相关选段 |
| <a id="r16"></a>R16 | Thomas–Yau，[Special Lagrangians, stable bundles and mean curvature flow](https://arxiv.org/abs/math/0104197) | 猜想、相位与流的相关选段 |
| <a id="r17"></a>R17 | Joyce，[Conjectures on Bridgeland stability for Fukaya categories of Calabi–Yau manifolds, special Lagrangians, and Lagrangian mean curvature flow](https://arxiv.org/abs/1401.4949) | 修正框架与奇点问题的相关选段 |
| <a id="r18"></a>R18 | Leung–Yau–Zaslow，[From special Lagrangian to Hermitian–Yang–Mills via Fourier–Mukai transform](https://arxiv.org/abs/math/0005118) | 半平坦模型及秩一方程选段 |
| <a id="r19"></a>R19 | Collins–Jacob–Yau，2015 预印本，[(1,1) forms with specified Lagrangian phase: A priori estimates and algebraic obstructions](https://arxiv.org/abs/1508.01934) | 作者、摘要及超临界相位／次解范围 |
| <a id="r20"></a>R20 | Bershadsky–Cecotti–Ooguri–Vafa，[Kodaira–Spencer Theory of Gravity and Exact Results for Quantum String Amplitudes](https://arxiv.org/abs/hep-th/9309140) | 振幅、全纯反常与歧义的相关选段 |
| <a id="r21"></a>R21 | Yamaguchi–Yau，[Topological String Partition Functions as Polynomials](https://arxiv.org/abs/hep-th/0406078) | 五生成元、权重、亏格范围、归一化及歧义选段 |
| <a id="r22"></a>R22 | Guo–Janda–Ruan，[Structure of Higher Genus Gromov–Witten Invariants of Quintic 3-folds](https://arxiv.org/abs/1812.11908) | 摘要中的三个结构结果；未把 conifold gap 记为已证结论 |
| <a id="r23"></a>R23 | Zagier，[Elliptic Modular Forms and Their Applications](https://people.mpim-bonn.mpg.de/zagier/files-restricted/doi/10.1007/978-3-540-74119-0/fulltext.pdf) | 模形式／拟模形式环的相关选段 |

文献事实与证明效力仍以各原论文的精确假设为准。本次没有重算 Gromov–Witten
不变量、构造新度量、运行几何流或完成形式化证明。

## 9. 收录与使用边界

本文的中文说明、问题组织、初等代数例子及登记元数据是此次新写的贡献。
数学定义、公式和书目信息用于说明公开的数学事实；第三方的诗、回忆原文、论文正文、
插图与版式未纳入发布单元。外部链接仅定位来源，不赋予其目标任何新许可。

唯一目录归属为 `geometry`，谱系种类为 `external-reference`，无推导父项。
文献中已证定理的身份，与本仓库将这篇说明登记为 `proposed-document` 的身份不同：
后者不改变前者，也不表示本仓库已经验证前者。目录检查只检验结构、归属和字节指纹。
本文没有原生数学准入、可执行证书或新的几何增长结论；Pascal 根增长义务仍为
`Open`，native `Seal` 为 `NotIssued`。

发表依据及精确文件指纹见
[准入记录](governance/publication/records/calabi-yau-fifty-years-reading-2026-09-20.json)。
该记录是 Codex 的发布内容审查，不是独立数学评审。任何后续可执行研究都须另定问题、
输入条件、检查器和有限资源范围，不能仅凭本文的登记获得证明或执行权限。
