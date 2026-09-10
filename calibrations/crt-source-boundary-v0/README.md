# Coprime reconstruction and source fidelity are separate obligations

Status: finite arithmetic calibration of a proposed mapping, 2026-09-10.
Direction: Mingli Yuan. Formalization and bounded check: ChatGPT.

The library main at `ba5be9fb672520ed22a7f2d923c1481bbe03aacc` adds the
al-Khwarizmi, Jiuzhang and Qin Jiushao trilogy. Those entries remain
proposed-document. This note tests one possible *literal inference* from
the Qin Jiushao entry's third correspondence: whether coprime observation
moduli alone make the reconstructed answer faithful to its source. It does
not decide the historical claims or invalidate the mapping as a heuristic.

## Frozen problem

Work in exact integers; observations are residues in Z/mZ. For positive
coprime m,n > 1, let M=mn and freeze the source domain to 0 <= x < M.
An observation is the ordered pair (x mod m, x mod n). The constructor uses
the two modular inverses and returns the least nonnegative CRT representative.
The independent checker enumerates every integer in the declared source
interval and groups its observed residue pair.

First instance: (m,n,x)=(3,4,5). Reuse instance: (5,7,17). In each instance,
replace only the first observed residue by (r+1) mod m. Ask separately:

1. Does the altered pair still have a unique reconstruction in [0,M)?
2. Does that reconstruction equal the fixed source x?
3. Does x+M, outside the declared interval, have the same honest observation?

One route; at most 256 enumerated nodes and five seconds for construction,
checking and output. A separate diagnostic uses moduli (4,6) on [0,24),
retaining its two-solution fibre rather than attempting an unavailable inverse.
The executable enforces the node limit; use the shell timeout for the hard
time bound. No native call, floating point, theorem search or game execution.

## Meaning of the result

For (3,4), source 5 produces (2,1). The altered pair (0,1) uniquely selects 9.
For (5,7), source 17 produces (2,3). The altered pair (3,3) uniquely selects 3.
Both pairs of moduli are coprime. Thus a unique arithmetic answer can be
the answer to a changed question. Coprimality does not certify that the supplied
residues were obtained faithfully from the declared source.

Further, x and x+M always share these observations. The finite interval is an
essential part of the uniqueness statement; a coverage declaration cannot be
silently widened. For (4,6), residues (1,5) select both 5 and 17 in [0,24).
They select one residue class modulo 12: non-coprimality does not itself mean
that no solution or useful observation exists.

The seeking-one operations are typed modular inverses: M/m is invertible
modulo m and M/n modulo n in the coprime instances. Their product is congruent
to 1 in the relevant quotient, not necessarily equal to integer 1. Zero and
nonunits have no such inverse. All multiplication here is commutative integer
arithmetic; nothing licenses reordering noncommutative histories elsewhere.

For the proposed Adva correspondence, three distinct obligations remain:
source-to-observation fidelity; reconstruction within a stated domain;
independent checking of the claimed result. Multiple checks, coprime moduli
or a narrow answer fibre alone discharge only their own declared obligation.
No relation equating checker independence with coprimality has been constructed
by this calibration. Native free and all nine symbol-surface obligations remain
unchanged. No new native word or universal grammar theorem is claimed.

## Replay and costs

From the library root:

```sh
timeout 5s python3 calibrations/crt-source-boundary-v0/calibrate.py
```

`report.json` retains both instances, exact inverse coefficients, honest and
altered fibres, alias witnesses, the noncoprime diagnostic, actual node count,
elapsed phase times and measured Linux process RSS. Every inverse is checked
by multiplication; every CRT output in both full finite domains is checked
against an independently enumerated fibre. The second instance reuses the
same constructor and checker. Costs of research, network retrieval and report
serialization are unmeasured. There is no speedup claim.

This helps readers distinguish an arithmetic reconstruction guarantee from
a claim that its inputs describe the intended object. The next mathematical
step would specify one concrete source-to-projection witness and its refusal
condition, rather than adding another independent-looking checker. Actual
utility for Jiamin's task has not been measured.
