# 黄金分割数与 AEG／adva：概念关系、已有结果与有限见证

研究日期：2026-09-10。问题提出：苑明理；整理、推导与有限计算：ChatGPT。

**结论：可以把黄金分割组织为一组共享精确算术、但保持不同解释边界的研究模块。最成熟的连接是：二次域 → 连分数／矩阵 → 正逆迭代 → 长方形分割；纽结字、螺线、替换语法和搜索分别通过声明过的接口接入。**

本文将“纳入”限定为：进入带有对象、关系、假设、证据与残差的研究组织；不表示这些内容已经成为原生 adva 词汇、已有完整形式化证明，或能够全部互相等同。未修改仓库或公开任何新内容。

## 1. 阅读范围与来源纪律

以用户指定的 [Golden ratio](https://en.wikipedia.org/wiki/Golden_ratio) 为检索目录，检查其正文、公式、图注及应用／争议部分；定位版本为 [oldid=1370346489](https://en.wikipedia.org/w/index.php?oldid=1370346489&title=Golden_ratio)。补充阅读 [Logarithmic spiral](https://en.wikipedia.org/wiki/Logarithmic_spiral) 与 [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence) 中相关构造。

下面的逐段索引按“共享一个论证的段落组”归并，不是原文翻译或百科重写。数学内容采用本文独立推导、AEG 原始文本以及文末一手论文支撑；历史、审美、自然观察保留为来源／测量任务，不从它们导出算术定理。没有递归遍历全部外链。

状态：**已有**＝已在核对的 AEG 正文中陈述并论证；**推导**＝本文给出数学推导；**有限验证**＝附件执行覆盖所列实例；**待接入**＝需要实现、额外证明或测量；**保留／纠正**＝不能按原陈述导入。

## 2. aeg-paper 已有的黄金分割结果

核对的 AEG 主线为 `609ac96b4df802a8a4a6c4079c43c2fae466bc3a`。以下路径均以这个版本为准。“golden”代码检索得到七个文件，另核对了当前纽结正文、计算附录及历史图源；这一关键词检索本身不保证找到所有纯符号写法。

| 来源 | 已出现的内容 | 本轮如何继承 |
|---|---|---|
| [Paper 0 §05](https://github.com/mountain/aeg-paper/blob/609ac96b4df802a8a4a6c4079c43c2fae466bc3a/paper-0/sections/05-reciprocals-fixed-points.tex) | $F(z)=1+1/z$；不动点 $\varphi$ 与 $1-\varphi$；连分数与 Fibonacci 比值 | **已有**。保留起点、非零分母、收敛条件和根的选择 |
| [Paper 0 附录 A](https://github.com/mountain/aeg-paper/blob/609ac96b4df802a8a4a6c4079c43c2fae466bc3a/paper-0/appendices/app-A-calculations.tex) | 一孔递归的矩阵乘法；连分数系数递推；仿射映射的幂 | **已有**。作为编译与独立回放的共同基础 |
| [Paper III §08](https://github.com/mountain/aeg-paper/blob/609ac96b4df802a8a4a6c4079c43c2fae466bc3a/paper-3/sections/08-threading-and-knot-questions.tex) 与 [附录 C](https://github.com/mountain/aeg-paper/blob/609ac96b4df802a8a4a6c4079c43c2fae466bc3a/paper-3/appendices/app-C-affine-quandle-calculations.tex) | 字 `abbbaBAAB` 的仿射残差 $-(t^2-3t+1)$ | **已有**。只在根处满足所选关系；不把一般参数处的残差称为纽结不变量 |
| [历史笔记 07](https://github.com/mountain/aeg-paper/blob/609ac96b4df802a8a4a6c4079c43c2fae466bc3a/notes/knots-and-loops/07-figure-eight-arithmetic-interpretation.tex) | 上述八字结算术解释；参数 $(3\pm\sqrt5)/2$ | 保留被正文重新验证的部分；“扫描更多纽结”的旧主张仍需脚本与版本证据 |
| [历史笔记 04](https://github.com/mountain/aeg-paper/blob/609ac96b4df802a8a4a6c4079c43c2fae466bc3a/notes/knots-and-loops/04-figure-eight-hnn-arithmetization.tex) | $u:x\mapsto x+1$、$v:x\mapsto x+\varphi$、$t:x\mapsto\varphi^{-2}x$ 满足指定 HNN 关系 | 保留精确特解，以及同篇明确指出的“不忠实”障碍：两个平移交换 |
| [历史笔记 03](https://github.com/mountain/aeg-paper/blob/609ac96b4df802a8a4a6c4079c43c2fae466bc3a/notes/knots-and-loops/03-figure-eight-aeg-summary.tex) | 用黄金参数校准八字结背景几何、传播与单值化的设想 | **待构造**。不能把设想写为已经建立的几何模型 |
| [历史笔记 05](https://github.com/mountain/aeg-paper/blob/609ac96b4df802a8a4a6c4079c43c2fae466bc3a/notes/knots-and-loops/05-figure-eight-modulo-arithmetization.tex) | 模 $(1,\varphi)$ 的二维表征及“稠密奇点”设想 | 必须纠正：二维格离散；某些一维投影稠密不是二维商空间奇异的证明 |
| [历史图源](https://github.com/mountain/aeg-paper/blob/609ac96b4df802a8a4a6c4079c43c2fae466bc3a/images/sources/knot_4_1.tex) | 使用约 $2.618$ 的比例绘制算术路径 | 作为图示来源；有限小数不是精确代数证书 |

以上状态服从 [Paper III 来源审计](https://github.com/mountain/aeg-paper/blob/609ac96b4df802a8a4a6c4079c43c2fae466bc3a/governance/paper-III-source-audit.md)。还必须继承三项修正：若乘法因子 $t=e^\lambda$，则 $t=\varphi^2$ 对应 $\lambda=2\log\varphi$；纤维提升不自动成为全测地双曲平面；$z\mapsto-1/z$ 是全纯映射，不能称为二维取向反转。

## 3. 逐段阅读后的纳入索引

本表只标识条目主题与我们自己的处理决定。每一行给出该主题在 adva 中可以提出什么任务；数学义务在后文展开。文中的“段”按逻辑内容定位，公式和紧邻图注归入同组。

| 条目位置／段落主题 | 在当前体系中的任务与归位 |
|---|---|
| 导言：比例、定义、符号 | 固定正长度与无量纲比值；符号名不代替根选择 |
| 导言：几何出现 | 建立精确坐标与 incidence 证书，不从图形外观验收 |
| 导言：自然与创作 | 建立观察记录和人为 specification，保持两类来源独立 |
| Calculation：等式变换、二次方程、两根 | 构造可回放改写；记录被除数非零及正根条件 |
| History：引言及古希腊段 | 进入 provenance；不新增数学原语 |
| History：Abu Kamil／Fibonacci 段 | 进入来源链；不把不同发现时间混作同一作者成果 |
| History：Pacioli／Leonardo 段 | 原始文本与后世解读分开登记 |
| History：Bombelli 段 | 几何算法历史索引；实际接入以坐标见证为准 |
| History：Jacob／Kepler／Maestlin 段 | 区分递推、收敛结果、有限小数三类对象 |
| History：de Moivre／Euler／Binet 段 | 闭式与递推的同值证明另列；命名不决定优先权 |
| History：Barr／phi／tau 段 | 建立 alias，不复制语义对象 |
| History：Zome／Penrose／准晶段 | 归入构造、替换、测量的不同接口 |
| Irrationality：最简分数与无限下降 | 证明任务使用自然数良基性；不能靠无限运行完成 |
| Irrationality：$\sqrt5$ | 保留另一条独立证明路径 |
| Minimal polynomial：多项式、代数整数 | 精确域编码与规范形；环与域的可逆性分开 |
| Minimal polynomial：范数、单位 | 提供 typed inverse；域的非零元不等于整数环的单位 |
| Conjugate and powers：共轭、倒数、小数部分 | 至少区分域共轭、复共轭、倒数及历史逆操作 |
| Conjugate and powers：幂递推与分解 | 固定阶数表达；另计系数位长增长 |
| Continued fraction：两种展开、收敛分数 | 一孔程序、矩阵前缀、尾部覆盖、有限区间证书 |
| Continued fraction：Hurwitz 段 | 分母预算下的逼近性质；不解释为计算本身困难 |
| Continued square root 段 | 另一个 fixed-point 程序；平方根类型与根号深度成本另计 |
| Fibonacci／Lucas：初值与递推 | 共享递推器，不同初值不合并为同一历史 |
| Fibonacci／Lucas：比值极限与交错 | 保存上下界与停止条件 |
| Fibonacci／Lucas：闭式、Pell、幂、和式 | 各自给出递推／共轭／余项证明；不以四舍五入替代 |
| Fibonacci／Lucas：螺线图注 | 保存圆弧拼接程序，与精确对数螺线分型 |
| Geometry／Construction：内分步骤 | 构造有向线段、圆与交点；验证长度与范围 |
| Geometry／Construction：外分步骤 | 另记交点分支与方向，不复用内分结论的量词 |
| Golden angle：角度定义 | 先用“周”为单位，$\alpha=\varphi^{-2}$；弧度读出再引入 $\pi$ |
| Golden angle：植物解释 | 测量和生成机制义务；不得直接作为最优性定理 |
| Pentagon／pentagram：对角线、相交、Ptolemy | 圆内接条件＋二次方程；可接线圆 incidence，不能自动等同 Pascal |
| Pentagon：三角函数值 | 单位根扩域与实部投影；不得替换 AEG 的 $q=4$ 契约 |
| Golden triangle／gnomon：角、边、分割 | 带类型的两个 tile 及切割见证 |
| Penrose：原型、kite/dart、Robinson、rhombi | 全部登记为有限 patch／匹配规则任务；尚未实现全平面验收 |
| Odom construction | 一个小型直线—圆求交任务，见第 8 节 |
| Kepler triangle：边、面积、角 | 引入 $\sqrt\varphi$ 前检查扩域；平方长度已在二次域 |
| Kepler triangle：极值段 | 另设一元优化问题和可行域，不能由勾股等式自动推出 |
| Golden rectangle | 正逆连分数、nested sets、残余面积与定向 frame |
| Golden rhombus：角、面积、内切圆 | 对角线契约；不要混同 Penrose 的两类菱形 |
| Golden rhombus：多面体段 | 有限面片组合和粘合证书；不由单面的比例推出整个多面体 |
| Vesica piscis | 交圆坐标与有向距离；明确所选交点 |
| Golden spiral：精确曲线与圆弧 | 区分连续流、离散轨道与显示近似 |
| Golden spiral：不同转角变体 | 将“每转多少角增长多少”作为参数，不只存 golden 名字 |
| Dodecahedron／icosahedron：坐标与度量 | 精确顶点、边、面计数；半径／面积／体积采用一致归一化 |
| Dodecahedron／icosahedron：三个长方形 | 纳入 Borromean 链候选；不宣称就是 M6 三机空间 |
| Dodecahedron／icosahedron：内接立方体、八面体 | 可复用 incidence checker；新增面格与对应方向 |
| Other properties：Newton／Halley／大数记录 | 研究算法成本和证书，不追逐当前位数纪录 |
| Other properties：五次／十次单位根 | 明确 cyclotomic field 与 real subfield 的投影 |
| Other properties：Gamma | 先执行函数方程消元；排除极点；不增加 Gamma 求值器 |
| Other properties：phinary | 位串→值与规范形→位串分开；位集和符号规则先固定 |
| Other properties：双曲几何 | 必须纠正度量对象混用，见第 9 节 |
| Other properties：Rogers–Ramanujan、模变换 | 有限连分数可编译；解析极限、分支与模群作用列为外部义务 |
| Other properties：Pisot | 共轭衰减可以解释近整数现象；不得把近整数当整数 |
| Architecture 各段 | 接入设计约束／历史证据，不设“美的验收器” |
| Art 各段及画幅统计 | 接入数据、误差与选择偏差；不导入艺术史争论的结论 |
| Books and design／Flags | 将设计意图、实际尺寸、单位分为字段 |
| Music：结构分析各段 | 编码分段、节拍与分析者假设；尚无实测收益 |
| Music：音程段 | 比值到 cents 的对数换单位；不是比例的算术同一 |
| Nature 各段 | 每个物种／样本单列观察；不接受自然界普遍定律 |
| Physics 两段 | 外部 E8 实验案例；保留条件和误差，不推出 AEG 物理模型 |
| Optimization：球面与搜索 | 球面采样是候选；一元搜索有单峰契约，见第 10 节 |
| Disputed：身体／贝壳／书页／审美／市场 | 全部作为 model-gap 与反驳材料，不作为支持普遍性的证据 |
| Egyptian pyramids 各段 | 测量对象与替代模型先固定；不继承历史意图推断 |
| Parthenon 各段 | 保留来源审计任务；不从比例拟合证明古人使用该数 |
| Modern art 各段 | 命名、构图与作者意图分开；不借用“黄金”名称赋予真值 |
| See also：metallic／silver | 同一矩阵模板的参数化复用，验证不依赖只挑黄金实例 |
| See also：plastic／supergolden | 三次扩域的未来类型测试；不塞入二系数编码 |
| Notes：正负根、别名、古典出处 | 合并到根选择与 provenance，保持原文与别名不混淆 |

上述索引使每个正文主题都有去处；不是所有主题都进入执行内核。后文给出能立即工作的共同数学核心。

## 4. 精确代数核心与四种不同的“反向”

令 $K=\mathbb Q[u]/(u^2-u-1)$，取实嵌入 $1<u<2$，记其像为 $\varphi$。最小多项式在有理数上不可约：若有有理根，由有理根定理只能为 $\pm1$，两者均不是根。

每个元素唯一写成 $a+b\varphi$。乘法为

$$ (a+b\varphi)(c+d\varphi)=(ac+bd)+(ad+bc+bd)\varphi. $$

域共轭 $\sigma(a+b\varphi)=(a+b)-b\varphi$；范数 $N(a+b\varphi)=a^2+ab-b^2$。非零元素的逆为

$$ (a+b\varphi)^{-1}=\frac{(a+b)-b\varphi}{a^2+ab-b^2}. $$

在域中非零便可逆；在整数环 $\mathbb Z[\varphi]$ 中要求逆仍在该环，则需范数 $\pm1$。这是一项类型边界，不能省略。

| 操作 | 对 $\varphi$／程序的作用 | 保留的结构 |
|---|---|---|
| 域共轭 $\sigma$ | $\varphi\mapsto1-\varphi=-\varphi^{-1}$ | 有理系数代数关系 |
| 实数倒数 | $\varphi\mapsto\varphi^{-1}$ | 乘法逆；非零前提 |
| 复共轭 | $\varphi$ 不变，$i\mapsto-i$ | 实部；二维取向改变 |
| 程序求逆 | 逆序执行每个逆操作 | 可逆程序的作用；需要定义域与原历史 |

尤其 $N(\varphi)=-1$，而 $N(\varphi^2)=1$。因此乘法归一不能把 $\varphi$ 的域共轭直接当成其倒数；平方后才有 $\sigma(\varphi^2)=\varphi^{-2}$。

固定两系数表示不代表常量空间：例如 $\varphi^n=F_n\varphi+F_{n-1}$，系数位长随 $n$ 线性增长。完整历史、输出位数和算术步数分别记账。

## 5. 连分数、AEG 一孔程序与八字结

一孔模板 $F_{a,b}(x)=a+b/x$ 对应矩阵 $M_{a,b}=\begin{pmatrix}a&b\\1&0\end{pmatrix}$，$b\ne0$。若按时间顺序先执行 $F_1$ 再 $F_2$，编译产物是 $M_2M_1$。字符串的左右阅读方向必须另存，不能凭矩阵外观猜测。

黄金实例 $F(x)=1+1/x$ 的矩阵为 $M=\begin{pmatrix}1&1\\1&0\end{pmatrix}$。对 $n\ge1$，归纳可得

$$ M^n=\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}. $$

取行列式便得 Cassini 恒等式 $F_{n+1}F_{n-1}-F_n^2=(-1)^n$；于是相邻比值的间距恰为 $1/(F_nF_{n+1})$。这些有理区间提供独立于浮点的有限观察证书。

必须区分两个问题：

* **固定种子**：从 $x_0=1$ 执行六步，末两值给出 $21/13<\varphi<13/8$，宽度 $1/104$。
* **尾部尚未给定**：只知道六个相同操作、末端孔可取任意 $x>0$，则 $F^6(x)=(13x+8)/(8x+5)$ 的全部像是 $(8/5,13/8)$。不能偷用前一任务的更窄区间。若尾部域改为复数或包含负数，该正区间覆盖证明就失效。

后一项是 `coverage-gated-close` 可直接复用的任务。越来越多的前缀带来更小的合法像，但有限前缀不自动规定整个无限尾部。

对纽结，定义 $a(x)=tx,b(x)=x+1,A=a^{-1},B=b^{-1}$，复合从右向左作用。逐项仿射乘法得到

$$ abbbaBAAB(x)=x-(t^2-3t+1). $$

同时

$$ M^2=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad \det(tI-M^2)=t^2-3t+1. $$

这就精确连接了 Paper 0 与 Paper III：$\varphi$ 是一孔不动点，而 $\varphi^{\pm2}$ 是两步矩阵的特征值，也是该关系字成立的参数。附件验证两个根以及错误参数／删除操作两个反例。

旧 HNN 特解也纳入：取 $u(x)=x+1,v(x)=x+\varphi,t(x)=\varphi^{-2}x$，则 $t^{-1}ut=uv$ 与 $t^{-1}vt=vuv$ 分别化为 $\varphi^2=1+\varphi$ 和 $\varphi^3=1+2\varphi$。但 $uv=vu$，所以纤维自由群中的交换子在这个表示中消失。增加标量精度不能恢复已经被商掉的非交换历史。

## 6. 长方形：正向增长、逆向切割与真正的有限边界

用 $(L,S)$ 记录长短边。正向拼接为 $P(L,S)=(L+S,L)$，矩阵正是 $M$。反向去掉一个正方形为 $C(L,S)=(S,L-S)$，矩阵为 $M^{-1}$。在 $L/S=\varphi$ 时，

$$ C(\varphi s,s)=\varphi^{-1}(\varphi s,s). $$

这说明整幅图的尺寸缩小，但在形状坐标 $r=L/S$ 上，去方块对应 $G(r)=1/(r-1)$（这一长短边分支要求 $1<r<2$）。

$$F'(\varphi)=-\varphi^{-2},\qquad G'(\varphi)=-\varphi^2.$$

**正向比例误差衰减，反向比例误差放大。** 大小的收缩与表征的稳定性是两个不同问题。对近似输入 $13/8$，切割比值依次为 $13/8,8/5,5/3,3/2,2,1$，随后已是正方形，不能把公式继续当作同类黄金切割。这给“无限分割”提供了一个直接的反例控制。

为保存位置和方向，在复平面固定

$$R_0=[0,\varphi]\times[0,1],\qquad S(z)=\varphi+\frac{i}{\varphi}z.$$

它把 $R_0$ 映到右侧余矩形 $[1,\varphi]\times[0,1]$，每步逆时针转 $\pi/2$、缩小 $\varphi^{-1}$。定义 $R_n=S^n(R_0)$。极限点为

$$z_* =\frac{\varphi}{1-i/\varphi}=\frac{1+3\varphi}{5}+i\frac{2+\varphi}{5}.$$

有 $R_{n+1}\subset R_n$，并且

$$\operatorname{area}(R_n)=\varphi^{1-2n},\qquad
\operatorname{diam}(R_n)^2=(\varphi^2+1)\varphi^{-2n}.$$

前 $n$ 块正方形的面积加上余矩形，精确等于原面积：

$$\sum_{j=0}^{n-1}\varphi^{-2j}+\varphi^{1-2n}=\varphi.$$

边界点采用闭集表示时可以共享；要求分割严格不相交时应规定半开边界归属。面积等式不能替代位置上的覆盖，但本构造的逐步包含与切割给出了覆盖理由。

因此 $\bigcap_nR_n=\{z_*\}$，这是平面内的普通点；螺线／对数坐标在此失效不等于底层平面有几何奇点。对任意 $\epsilon>0$，只需在 fuel 内找到 $n$ 使 $(\varphi^2+1)\varphi^{-2n}\le\epsilon^2$，便能报告有限分辨率已满足。附件验证 $n=12$ 时直径小于 $0.01$；任一有限步的余面积仍严格大于零。

## 7. 对数螺线、黄金螺线、Fibonacci 圆弧与对数坐标

由上述仿射递推，

$$S^n(z)=z_*+(i/\varphi)^n(z-z_*).$$

选定每步转 $\pi/2$ 的连续提升后，可以插值得到

$$z(s)=z_*+(z_0-z_*)\exp\bigl[s(-\log\varphi+i\pi/2)\bigr].$$

消去参数，就是收缩方向的黄金对数螺线：$r=r_0\exp[-(2\log\varphi/\pi)(\theta-\theta_0)]$。逆向执行得到增长方向。同一离散乘子还允许加上 $2\pi k$ 的角度提升；仅有离散点不能唯一规定连续插值。

一般对数螺线写成 $z(\theta)=r_0e^{b\theta}e^{i\theta}$，$r_0>0,b\ne0$。直接微分可得 $|z'|=r\sqrt{1+b^2}$、曲率 $\kappa=1/(r\sqrt{1+b^2})$；与同心圆切线的夹角满足 $\tan\alpha=b$。一段的弧长是 $\sqrt{1+b^2}|r_2-r_1|/|b|$。无穷绕转可以具有有限总弧长，但程序步数、绕数和资源不会因此成为零。

“黄金”需要两个参数：比例 $\varphi$ 与转角。每 $90^\circ$、$108^\circ$ 或 $180^\circ$ 放大 $\varphi$ 给出不同的 $b$，应保存为不同曲线。

三类对象不能合并：

| 对象 | 精确可保存的数据 | 未完成的义务 |
|---|---|---|
| 黄金对数螺线 | 连续流公式、中心、方向、对数提升 | 一般角度的超越函数求值误差 |
| 黄金方块圆弧拼接 | 方块大小 $\varphi^{-n}$、圆心、起终角 | 与目标螺线的指定误差度量 |
| Fibonacci 圆弧拼接 | 整数方块 $F_n$ 和四分之一圆 | 比例逼近误差＋圆弧模型误差两项 |

相邻圆弧切向可以接续，但曲率分别为 $1/F_n$ 和 $1/F_{n+1}$，一般有跳变；精确对数螺线远离中心时曲率连续。即使把方块比例改为精确黄金比例，圆弧仍不会变成对数螺线。只增加同类方块不会自动使归一化的圆弧形状误差趋于零。[S1] 研究的正是这类近似及其一般化。

在覆盖坐标 $u=\log(r/r_0),v=\theta\in\mathbb R$ 上，螺线变成直线 $u=bv$。这是 AEG 可用的表示转换：乘法尺度变成加法，角度的圈数变成整数历史。投影回平面会把 $v$ 与 $v+2\pi k$ 识别；若不保存 $k$，就不能声称保留绕行历史。

还应区分圆反演 $z\mapsto1/\bar z$ 和全纯倒数 $z\mapsto1/z$：前者保持角度、反转径向尺度，后者同时改变角度符号；AEG 的 $-1/z$ 又多一个半周旋转。

## 8. 其他几何关系如何化成算术任务

**线段构造。** 长度 $a>b>0$ 的比例条件等价于 $a^2=ab+b^2$。给定单位长度后，尺规构造可转为线圆交点的二次方程；交点符号和所在射线必须作为证书。Euclid VI.30 是原始几何来源 [S2]。

**五角形与三角形。** 对单位边长的正五边形，用圆内接四边形的 Ptolemy 等式得到 $d^2=d+1$，故正对角线 $d=\varphi$。这条路径依赖“共圆与正五边形”，不能推广给任意五边形。令 $\zeta=e^{2\pi i/5}$，$\zeta+\zeta^{-1}=\varphi-1$；其满足 $s^2+s-1=0$，由 $1+\zeta+\cdots+\zeta^4=0$ 消元可得。整个 $\mathbb Q(\zeta)$ 是四次域，实部子域才是 $K$。因此五折旋转与实数黄金参数相连，但 $q=5$ 的 Hecke 参数 $2\cos(\pi/5)=\varphi$ 不能直接替换 AEG 已有的 $q=4$ 参数。

**Odom 构造。** 取等边三角形顶点 $(0,\sqrt3),(\pm1,0)$，两腰中点为 $(\pm1/2,\sqrt3/2)$；外接圆中心 $(0,\sqrt3/3)$、半径 $2\sqrt3/3$。中点连线与圆相交处的横坐标是 $\pm\sqrt5/2$。因此沿该线出现长度 $1$ 与 $(\sqrt5-1)/2$，精确比值为 $\varphi$。这是可直接提交给 incidence checker 的小问题；坐标需扩入 $\sqrt3$，不要假装都在 $K$ 中。

**Kepler 三角形。** 若直角三角形边长按 $1,r,r^2$ 成等比，则勾股关系给 $r^4=r^2+1$，所以 $r^2=\varphi$，边为 $1,\sqrt\varphi,\varphi$。平方边长已在 $K$，实际长度需要扩域；面积和极值问题另列。关于“两份拼成的等腰三角形”的优化命题暂不作为本轮验收结果。

**黄金菱形。** 取顶点 $(\pm\varphi/2,0),(0,\pm1/2)$；两对角线比为 $\varphi$，边长平方 $(\varphi^2+1)/4$，面积 $\varphi/2$。这些等式属于低成本校准；与 Penrose 菱形的角度定义不同。

**交圆。** 取两单位圆中心 $(\pm1/2,0)$，交点纵坐标 $\pm\sqrt3/2$；同心二倍半径圆交点纵坐标 $\pm\sqrt{15}/2$。从下方单位圆交点到上方二倍圆交点的线段被上方单位圆交点分成 $\sqrt3$ 与 $(\sqrt{15}-\sqrt3)/2$ 两段，比为 $\varphi$。交点顺序选错就不再是同一个命题。

**正二十面体。** 取十二点

$$ (0,\pm1,\pm\varphi),\quad(\pm1,\pm\varphi,0),\quad(\pm\varphi,0,\pm1). $$

附件逐对计算平方距离，得到 30 条长度 2 的边，且每点度数 5；边图包含 20 个三角面。归一到边长 $a$ 后表面积为 $5\sqrt3a^2$。对偶正十二面体、内外接球及内接立方体／八面体可继续使用精确坐标和面格，但本轮未逐一执行。

**三张黄金长方形与 Borromean 链。** 上述点分布在三个坐标平面中的长方形边界上。长方形的填充面可以相交，三个边界却互不相交；两者必须分型。这组边界与 Borromean 链的关系有一手论文 [S3]。它提供“任意两支可分，三支共同纠缠”的具体拓扑对象，但黄金比例不是产生该链型的唯一长宽比。本轮验证顶点与边面数据，没有构造链图、Reidemeister 回放或三重链接证书，因此不把它识别为 M6 的模型。

## 9. 双曲几何：三个不能混用的长度

统一采用曲率 $-1$ 的上半平面度量 $ds^2=(dx^2+dy^2)/y^2$。

矩阵 $N=M^2$ 的迹是 3，特征值为 $\varphi^{\pm2}$，其双曲平移长度为

$$\ell(N)=2\operatorname{arcosh}(3/2)=4\log\varphi.$$

可以不依赖数值来验证：把两个实不动点送往 $0,\infty$，作用成为比例 $\varphi^4$ 的伸缩（或其逆），沿竖直测地线积分 $dy/y$ 即得此长度。这是真正可接回 AEG 矩阵与八字结参数的尺度量。

但理想三角形 $0,1,\infty$ 中，内切圆三个切点为 $(0,1),(1,1),(1/2,1/2)$。由

$$\cosh d(P,Q)=1+\frac{|P-Q|^2}{2\operatorname{Im}P\operatorname{Im}Q}$$

得到切点三角形的边长 $2\log\varphi$。而在竖直边上的点 $(0,y)$ 到另外两边的距离分别为 $\operatorname{arsinh}(y)$ 与 $\operatorname{arsinh}(1/y)$；两者较小值的最大值为 $\operatorname{arsinh}(1)=\log(1+\sqrt2)$。

| 对象 | 数值表达 |
|---|---|
| $M^2$ 的双曲平移长度 | $4\log\varphi$ |
| 理想三角形内切圆切点所成三角形的边 | $2\log\varphi$ |
| 该理想三角形“边上点到另两边较近者”的最大距离 | $\log(1+\sqrt2)$ |

读取的百科段落将这些不同对象混在一起，不能照录。附件对切点距离的代数部分作了精确检查；上面的推导明确了度量归一化。这里的纠正不影响黄金参数与迹 3 矩阵的联系。

## 10. 有限语法、编码与搜索

**Fibonacci／Lucas 与 Pisot。** 两根 $\varphi,\psi=1-\varphi$ 都满足相同递推。由初值可验证 $F_n=(\varphi^n-\psi^n)/\sqrt5$、$L_n=\varphi^n+\psi^n$。于是 $L_n^2-5F_n^2=4(-1)^n$，而 $|\varphi^n-L_n|=\varphi^{-n}$。共轭小于 1 的性质解释近整数，却不允许删去仍非零的余项。$n\ge2$ 时余项小于 $1/2$，才可证明最近整数的判断。无限和应附几何级数尾项，不执行无界循环。

**替换语法。** 采用 `A -> AB, B -> A`，从 `A` 开始同步替换。计数向量由 $M$ 推进，实际词仍有次序。附件执行六步：最后有 13 个 A、8 个 B。不同词可能计数相同，所以计数矩阵是忘却后的表示，不能替代整词。Penrose 有额外的空间边匹配与朝向义务；de Bruijn 的一手论文 [S4] 给出其代数理论，本轮只登记可接入方案。

**phinary。** 因 $\varphi^2=\varphi+1$，位串 `100` 与 `011` 可有同值。编码必须指定允许正负位、正负指数、小数点及规范形；同值可判定不等于已证明重写系统终止合流。整数的 Zeckendorf 编码、$\varphi$ 进位编码与连续比例表示也不是同一个编码。

**Hurwitz。** 黄金比例是以分母大小衡量的有理逼近中的极端实例。这并不意味着计算其代数表达式或小数最困难；更不表示它是唯一具有同类极端性质的数。有限证书使用 Cassini 间距即可；完整 Diophantine 定理独立导入。

**另两条求值路线。** $H(x)=\sqrt{1+x}$ 在区间 $[1,2]$ 上导数绝对值不超过 $1/(2\sqrt2)$，给出带平方根成本的收敛方案。Newton 对 $p(x)=x^2-x-1$ 的更新为 $(x^2+1)/(2x-1)$，分母要求 $x\ne1/2$；Halley 则还需要检查 $2p'^2-pp''$ 不为零。要比较速度应统一精度、位运算与验证成本，而非只比较迭代次数。本轮没有做高精度算法竞赛。

**黄金分割搜索。** 取 $\rho=\varphi^{-1}$，在 $[a,b]$ 上比较

$$x_1=a+(1-\rho)(b-a),\qquad x_2=a+\rho(b-a).$$

在声明的严格单峰／单谷契约下，可缩小区间并复用一个旧函数值，因为 $1-\rho=\rho^2$。没有单峰契约、比较误差未定、函数版本或 frame 已变时，不能这样删去候选范围。Kiefer 的原论文 [S5] 区分固定观察次数的 Fibonacci 方案与可继续观察的黄金方案；不能把后者称为所有预算下的全局最优搜索。

本轮对 $f(x)=(x-r)^2$、$r=3/7$ 与新实例 $r=2/3$ 各执行 12 次区间收缩。相同任务、精确比较、相同区间轨迹下：不复用版本各调用 24 次，复用版本各调用 13 次。这里证明的是已定义任务中的旧观察复用，不是任意问题上的搜索加速，也不是学习定理。

**球面采样／黄金角。** 用“周”为单位令 $\alpha=\varphi^{-2}$，可构造 $\theta_n=2\pi\{n\alpha\}$；选 $z_n=1-2(n+1/2)/N$ 则每个纬带等面积，再令 $x_n+iy_n=\sqrt{1-z_n^2}e^{i\theta_n}$。这是明确定义的候选生成器；最小间距、能量、覆盖半径是不同优化指标，有限样本均匀外观不构成最优性证明。

## 11. 解析扩展、物理与语用

**Gamma 关系**无需先实现特殊函数。依据函数方程 [S6]，$\Gamma(z+1)=z(z-1)\Gamma(z-1)$。在两边有限且 $\Gamma(z-1)\ne0$ 的域上，等式 $\Gamma(z-1)=\Gamma(z+1)$ 等价于 $z^2-z-1=0$。若把极点的“无穷”等同，就改变了原问题，必须拒绝。

**Rogers–Ramanujan 连分数**给出比普通常系数连分数更大的前沿。有限截断仍是一串 $x\mapsto1+q^j/x$ 的矩阵；完整解析对象还需 $|q|<1$、第五根分支、收敛及模变换证明。Duke [S7] 具体联结这一连分数、二十面体方程与模函数，并给出特殊值的证明路径。可登记为 `Proposed` 解析模块；当前二次域与有限截断不自动覆盖它。

**自然与物理**接入 Observation，而不接入算术公理。Douady–Couder [S8] 的实验与模拟说明特定迭代机制可产生相关排列；其条件不能删除。Coldea 等 [S9] 在特定 Ising 材料与临界场附近观测到低能模比值接近黄金比例；这不证明所有物理系统、AEG 三机或 M6 都具有 E8 对称。

**艺术、建筑、音乐、历史**接入 specification／provenance／measure：例如主动把画幅规定为黄金比例，是设计约定；测量既有画幅再拟合比例，是统计判断；推断作者有意采用，是历史判断。三者不能互相替代。音程换算 $1200\log_2\varphi$ 只是比值到另一单位的读出，不增加关于审美的数学真值。

## 12. 本轮纠正与拒绝项

1. **百科的单位边长正二十面体面积公式不能直接导入。** 20 个等边三角面给出 $5\sqrt3$；读取版本所列 $10\varphi^2$ 与此不等。附件从十二顶点独立枚举边面，并以平方关系排除该公式。
2. **理想三角形的距离对象混用。** 正确区分见第 9 节。
3. **有限小数不是精确根。** 不能从浮点乘法得到 1，便验收 $t_+t_-=1$ 的原问题。
4. **边界小于 $\epsilon$ 不等于空。** 保留 residual 与相应量词。
5. **圆弧图不等于解析螺线。** 比例误差与模型误差分别记录。
6. **二维离散格不等于一维稠密投影。** 旧 AEG 笔记的拓扑结论必须按审计修正。
7. **相同特征多项式不证明同一空间或同一语义。** 特别不推出完整 Teichmüller／Calabi–Yau／M6 识别。
8. **算子闭合不抹除历史，也不授予原生 free。**

## 13. 三计算的工程组织与纳入顺序

下表是研究任务分工，不是声称三个数学对象已经证明同构。

| 工作面 | 保存什么 | 验收条件 |
|---|---|---|
| 构造 K | 精确域、表达式 AST、规范形、域扩张 | 独立代数等式、合法分母、嵌入选择 |
| 时间 t | 操作次序、前缀、迭代次数、函数版本、fuel | 回放相同；预算可界定；旧观察复用有作用域 |
| 空间 X | 坐标 frame、残余矩形／区间、角度提升、覆盖 | 包含、误差与边界证书；不遗漏合法候选 |

每一项收据至少绑定：`question_id, object_type, arithmetic_domain, embedding, expression_or_word, evaluation_order, frame, assumptions, fuel_used, claim_scope, witness, residual`。若用新术语，应是对这些关系的有见证压缩，而不是重复注册一个名字。

依赖顺序：

1. **第一批可落实**：精确二次域；Paper 0 连分数；Paper III 关系字；HNN 成功与不忠实控制；矩形有限切割／覆盖。
2. **第二批**：有提升历史的离散螺线；保留模型残差的显示层；有作用域的函数值复用；一元搜索合同。
3. **第三批**：线圆构造、三角形、正多面体；Borromean 链图与独立拓扑验收；Penrose patch 与匹配边界。
4. **第四批**：解析连分数、模函数、自然／物理测量；均先形成问题，不承诺本轮完成。

不需要先引入一个容纳所有对象的普遍空间。共享精确数域与可审计的转换，已经足以让这些问题共同工作。三次域、五次单位根、平方根和对数应是显式扩展，不偷偷进入同一原语。

## 14. 执行证据、成本与下一步

附件 `verify_golden.py` 仅使用 Python 标准库。运行：

```sh
python verify_golden.py > evidence.json
```

预算：30 秒；Fibonacci 身份到 $n=32$；矩形面积到 16 步；替换语法 6 步；两个二次函数各 12 步搜索；十二顶点的 66 对距离。无无界搜索。结果：**310 项明确断言通过**；执行期间没有修正回放。

* 域构造与最初校准：1.339 ms。
* 全部构造与验证：17.730 ms（包含前一项）。
* 序列化与解析回放：0.426 ms。
* 进程峰值 RSS：10,880 KiB，约 10.625 MiB。
* 两个实例分别：24 次函数求值降为 13 次，区间轨迹完全相同。相应局部运行时间为 1.641→1.273 ms 和 1.586→1.204 ms；单次微型测量不是通用性能结论。
* 研究、检索、写作以及词汇形成的人工成本未测量，不包括在毫秒统计中。

这些是外部 Python 见证，并非原生 adva 或 Rust 执行结果；没有跑原生 free，没有证明普遍语法。图示采用近似绘制，只用于解释，不能作精确验收依据。

最小下一步：在既有语法下形成 `golden-task` 与 `golden-witness` 的版本化任务对，先让同一个校验器区分“固定种子”“未知尾部”“精确闭合”“有限精度停止”四种收据。这样既接住 AEG 已有成果，也能直接暴露表示转换时可能越过的边界。

## 15. 一手来源与后续核对入口

* **[S1]** Reitebuch, Skrodzki, Polthier (2021), [Approximating Logarithmic Spirals by Quarter Circles](https://archive.bridgesmathart.org/2021/bridges2021-95.pdf)。本轮阅读，支持圆弧近似与解析曲线分型。
* **[S2]** Euclid, [Elements VI.30](https://aleph0.clarku.edu/~djoyce/elements/bookVI/propVI30.html)。构造原始来源；本轮可检索到命题，全文访问受限；本文使用独立代数推导。
* **[S3]** Gunn, Sullivan (2008), [The Borromean Rings: A Video about the New IMU Logo](https://archive.bridgesmathart.org/2008/bridges2008-63.pdf)。本轮阅读，含黄金长方形边界的关联。
* **[S4]** de Bruijn (1981), [Algebraic theory of Penrose’s non-periodic tilings of the plane, I, II](https://pure.tue.nl/ws/files/4344195/597566.pdf)。已核对来源；扫描页正文未作完整机器化核验，作为后续导入入口。
* **[S5]** Kiefer (1953), [Sequential minimax search for a maximum](https://scispace.com/pdf/sequential-minimax-search-for-a-maximum-58gl9exg7h.pdf)，Proc. AMS 4, 502–506，DOI `10.1090/S0002-9939-1953-0055639-3`。本轮读取原论文镜像。
* **[S6]** NIST DLMF, [§5.5 Functional Relations](https://dlmf.nist.gov/5.5)。Gamma 消元的函数方程；也需核对 §5.2 的极点与无零点条件。
* **[S7]** W. Duke, [Continued Fractions and Modular Functions](https://www.math.ucla.edu/~wdduke/preprints/bams4.pdf)。本轮阅读相关定义与定理入口，不声称完成全部模函数理论导入。
* **[S8]** Douady, Couder (1992), [Phyllotaxis as a physical self-organized growth process](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.68.2098)。本轮核对摘要，全文实验未复现。
* **[S9]** Coldea et al., [Quantum criticality in an Ising chain: experimental evidence for emergent E8 symmetry](https://arxiv.org/abs/1103.3694)。本轮核对作者摘要，实验未复现。
* **[S10]** Hurwitz (1891), [Ueber die angenäherte Darstellung der Irrationalzahlen durch rationale Brüche](https://eudml.org/doc/157573)。已定位原始文献记录，全文读取受限；完整定理导入仍列后续义务。

本文的新增是上述关系在当前 AEG／adva 工作边界中的组织、具体推导与有限见证，不主张这些经典数学关系是新的数学发现。
