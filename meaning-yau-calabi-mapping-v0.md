# 丘成桐 Calabi 历程的算术映射 v0（Yau-Calabi narrative mapping v0）

日期：2026-09-09。状态：`proposed-document`（proposed-mapping，待人类评审；
散文不被验证为真）。方向：Mingli Yuan；整理：assistant。
目录学条目：`logic-yau-calabi-mapping`（home=logic）。

## 1. 五锚点映射（每锚点 pin 到收据）

| 历程句 | 我们的陈述 | 算术锚点（精确分数） |
| --- | --- | --- |
| Einstein 系统 → 一个标量方程 | 三循环系统 → 标量不变量 | det((2I+C)/3) = 1/3；(2I+C)(4I−2C+C²) = 9I |
| Ricci 形式 = 拓扑不变量（第一陈类） | 绕数是路径的拓扑不变量 | w = ±1, ±2（半开约定） |
| c₁=0 → Ricci 平坦 | 零类局部规则 w=0 ⇒ 恒等 | A⁰ = I；Aʷ·A⁻ʷ = I |
| K3：第一个非平凡例 | 菱形见证：闭合 ≠ 恒等 | A(0,1) = (2,1) ≠ (0,1) |
| 好得难以置信 → 六年奠基 | 范围反例 + 收据链 | A·B1·A⁻¹·B1⁻¹ = ((13,8),(8,5)) ≠ I；收据链 01–17 |

校准收据：AEG 仓 `receipt-17.json`，sha
`ce3d76aab373ef5deb7cf0635e19242ce10f87067469ecf8c106a657251f81dd`。

## 2. 对偶谱支柱（receipt-18）

L = (2I+C)/3 的特征值 {1, 1/2 ± i√3/6}；对偶侧 L⁻¹ = (4I−2C+C²)/3
的特征值 {1, 3/2 ∓ i√3/2} = 3 × 共轭。能量 |λ|²：{1, 1/3, 1/3}
与 {1, 3, 3}，乘积 1/9 = det² 与 9 = det⁻²，**精确互逆**。"一正两负"
布局在三个绕数的零和（w0+w1+w2=0，如 +2, −1, −1）；第三生成元
（第三个 cusp）为开放槽。收据：AEG 仓 `receipt-18.json`，sha
`497bd138ee8e5c141523506cf2647c670e7d4b5495ad1296dab94f33b39dbc62`。

## 3. 边界

- proposed-mapping：本文件是"我们材料 ↔ 历程"的对应提议，**不是**
  与 Calabi-Yau 几何的等同声称；
- 散文不被验证为真；算术锚点由 AEG 收据 17/18 的字节 pin 支撑；
- 不入 claims.toml；无原生准入；无新纪元。
