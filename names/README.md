# names: party naming layer

`party-naming-layer-v0.json` 是三方命名层 v0（方案 A，2026-09-09 明理裁定）：
Machine→Substrate（基底）、World→Knowledge（知识）、Human→Surface（界面）。
pascal 原始字节不变；本目录只新增映射，不重命名任何目录或文件。登记为
math 目录学条目 `logic-party-naming-layer`（proposed-document）。
过程记录见 **protocol-engineering** 仓（旧名 `proto`，2026-09-11 改名）的
`party-naming-layer.md`（跨仓引用，字节不复制）。改名理由与反向操作见该仓
`naming-decision-2026-09-11.md`。


`catalog-key-words.json`：目录学 15 个 key 的显式源短语（链接操作的输入），
包括 `logic-yau-calabi-mapping`。`catalog-key-words-v1.json` 记录受限词法策略、
源文件字节 pin 与全部 15 项；两份文件登记为命名层条目的材料。

link/unlink 保持已声明词列的顺序与拼写。title 的意义如何成为这个词列，
仍需独立的解释契约；目录检查不验证散文、数学命题或社会信任。

The v1 domain is an ordered nonempty list of at most sixteen distinct tokens
matching `[a-z0-9]+`, with at most eighty characters in the joined key.
There is no normalization. The seven historical prefix exceptions are fixed.
The source document and v1 document each cover all fifteen current keys.

The outer Adva PR #166 supplies `math-check --key-words`; this library change
alone does not install that option. Default `math-check` only checks documentary
structure and pins. The optional v1 gate checks naming coverage and word/key
agreement, while source prose remains hash-bound and title semantics unchecked.

The 2026-09-09 continuation preserves all prior fourteen entries and appends
the newly registered key to both documents. The library base is `b3ff7ad`;
its earlier commits retain the preceding source bytes. Pascal materials and
the Open growth obligation remain unchanged. See Adva PR #166 and
`docs/research/catalog-key-words-alignment.md` for the paired baseline and
repair evidence, including a fresh sixteenth-key control.

## Symbol surface continuation

The current manifest and both naming documents now cover 17 keys.
`logic-symbol-surface-swap` is appended after the sixteen-entry baseline;
the source digest and the naming-layer material pins are updated together.
Earlier counts above describe historical checkpoints. No lexical policy changes.

## Period-three calibration continuation (2026-09-11)

The manifest and `catalog-key-words-v1.json` now cover **24 keys**; the
seventeenth-key paragraph above and the earlier counts describe historical
checkpoints and are not restated. The appended key is
`arithmetic-period-three-matrix-calibration`, recording an external bounded
calibration of the period-three interval graph and the golden one-hole matrix.

Two facts about coverage that the earlier sections do not state:

- The **v1 document and the manifest are the gated pair**: the checker requires
  v1 to cover every declared catalog key exactly once, and no foreign key.
- `catalog-key-words.json` remains the **earlier partial source** at 17 entries.
  It is registered material whose bytes are pinned, not a coverage gate, so a
  catalog larger than its source is consistent. Do not "repair" it by copying
  v1's list into it; that would rewrite a pinned historical input.

Admitting this entry required raising the catalog's declared read-file bound
from 96 to 120, because 95 of 96 slots were already spent. The raise is recorded
in `python/adva/math_catalog.py` and in the new entry's `open_obligations`, and
it is granted once rather than made a standing allowance.
