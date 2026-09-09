# names: party naming layer

`party-naming-layer-v0.json` 是三方命名层 v0（方案 A，2026-09-09 明理裁定）：
Machine→Substrate（基底）、World→Knowledge（知识）、Human→Surface（界面）。
pascal 原始字节不变；本目录只新增映射，不重命名任何目录或文件。登记为
math 目录学条目 `logic-party-naming-layer`（proposed-document）。
过程记录见 proto 仓 `party-naming-layer.md`（跨仓引用，字节不复制）。


`catalog-key-words.json`：目录学 14 个 key 的显式源短语（链接操作的输入）。
每个 key 是其短语的 link 像；这是显式命名声明，尚未验证 title 的语义。

`catalog-key-words-v1.json`：原文件保留不变，v1 固定 link/unlink 的输入域。
词只能含小写 ASCII 字母和数字，不含连字符；不自动转小写、去空格或做
Unicode 归一。保留词序，按当前命名政策拒绝重复词；最多 16 个词，key
最多 80 字符。重复限制是命名政策，不是可逆性的数学必要条件。
七个历史前缀例外保持显式且固定。

两个文件均登记到 `logic-party-naming-layer` 的 materials。新检查入口是
`python3 -S python/adva/adva.py math-check --key-words`，需要配套 Adva
实现；默认命令仍检查目录结构和摘要。v1 检查词序、可逆性、完整 key
覆盖与 home 对应，明确 `title_semantics_checked=false`。不授予原生身份，
不改变 Pascal 增长义务，也不把四条中文指令当作已实现的文言程序。
