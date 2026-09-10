# Integration account

Upstream Adva main: 7be406bfa6a3b7a5ef619081157e3b113da0cd40.
Upstream library main: ba5be9fb672520ed22a7f2d923c1481bbe03aacc.
Prior library PR #3 head: 2dc75bd9f0e446cbb4f43361ccdeee1119564c12.

Seven changed library files were retrieved and their Git blob hashes verified.
Main added three proposed catalog entries and refreshed existing pins; no real
native text-transfer package or PR comment arrived. The unchanged native
artifact was not fetched again.

The catalog was reconciled by key: preserve all current main entries and pins;
retain the PR's extended logic-symbol-surface-swap entry (main had not changed
that entry); attach this finite calibration only to the new Qin Jiushao entry.
The three upstream meaning documents and current topic/naming indexes remain
byte-identical. The main symbol-surface catalog report is preserved. Historical
17-entry and later transport reports remain separately dated records. The
current math README counts are corrected to 20 distinct entries/23 memberships.

Validation: 86 enumerated nodes under the 256-node bound, two coprime instances
covering all 47 states, one 24-state noncoprime diagnostic, 0.060311 ms before
report serialization, Linux peak RSS 7,936 KiB. Full exact inputs and output are
in report.json. CatalogConsistent: 20 entries, 84 referenced files, 5.097450 ms
before serialization. No native calls, new native words or full test-suite run.
Research, authoring, network and serialization costs are not included.

A two-parent merge commit retains both upstream main and the prior PR branch.
This updates the existing draft PR; it does not merge that PR into main or
change the outer repository's library gitlink.
