# Validation account

The receiving construction completed in 1.538 ms, including four rejection controls and serialization replay; receipt serialization took 0.128 ms. Linux process peak RSS was 10,880 KiB. A separate read-only replay completed in 1.521 ms with the same receipt hash and peak RSS. Zero native calls and zero search candidates. These measurements exclude authoring, network retrieval and report serialization.

The first catalog check returned Unknown because the material reference list exceeded the fixed per-list limit of 16. The implementation correction moved the imported execution report and prior text audit from materials to evidence, without changing the limit or their bytes. One correction replay returned CatalogConsistent: 17 entries, 72 referenced files, 1,982,346 bytes, 3.855 ms before serialization. See catalog-report.json. Its manifest pin identifies the checked manifest; this report is not self-indexed.

The check used a scoped outer Adva snapshot containing every catalog-referenced file. Vendor gitlinks were not materialized and a full native toolchain was unavailable. No Rust execution or complete repository test suite was performed in this round. The external math_catalog.py SHA-256 was d9ee0143d5636de04f7c8c403eeb9ed5c6d645639cdcd91e5d982df1ed501dba, matching the peer execution source inventory.

This work changes only README.md, the existing catalog entry and the new receipt directory. The historical handoff, all original symbol-surface source files, topic indexes, growth obligation and seal are unchanged. New native vocabulary and mathematical discharges: zero.
