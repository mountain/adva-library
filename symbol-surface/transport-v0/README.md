# Bounded text transport v0

Proposed external tooling, 2026-09-10. This implements the transport interface
requested after the library's native-load receiving acknowledgment. It changes
no Adva semantics, native artifact or historical receipt.

## Frozen question

Can a producer make exact pinned gzip bytes readable across the existing
text-only receiving interface, with explicit finite coverage and refusal?
The objects are byte strings, a versioned JSON manifest and ordered base64
parts. The scope is transport integrity relative to a separately fixed target;
it is not mathematical equivalence, build authentication or native admission.

One implementation route, two deterministic synthetic instances, five seconds
per command, at most 64 parts and 4 MiB encoded text, at most 65,536 bytes per
part and a 32 KiB manifest. No search or automatic continuation. The receiver
does not decompress, load or execute the bytes. The exact real artifact is
still unavailable locally, so its status remains NotReceived / Unknown.

## Producer and receiver contract

`transport.py` freezes the real target independently of the supplied manifest:

- Repository: `mountain/adva`, commit `e0e3433ebcaa2da6ec3e0bc1f67bd316f2c38547`.
- Path: `experiments/advance_symbol_surface/evidence/run-01/_native.abi3.so.gz`.
- Bytes: 2,039,917.
- SHA-256: `f31edc374020672cba9c783be8898243a33653b6548b9f25754db82c9302b423`.

Run the producer on a checkout holding that exact artifact, with a fresh output
directory. From the library root (replace the input path with its local path):

```sh
timeout 5s python3 symbol-surface/transport-v0/transport.py pack /path/to/_native.abi3.so.gz /path/to/fresh-text-parts
```

The producer verifies the frozen length and digest before writing anything.
Output is one manifest and numbered ASCII parts without newlines. For the
declared real artifact, base64 requires 2,719,892 characters in 42 parts;
these are calculated transport dimensions, not evidence of its reception.
Publish the new directory alongside the original gzip without replacing it.
If an I/O failure leaves partial output, retain that failure and choose a
separately authorized fresh directory; do not assume it is a complete package.

On the receiving side, after reading all declared text files into a directory:

```sh
timeout 5s python3 symbol-surface/transport-v0/transport.py verify /path/to/received-text-parts
```

The receiver requires exact file coverage, canonical part order and names,
per-part lengths/hashes, strict and canonical base64, and the independently
frozen decoded-byte length/hash. Duplicate JSON keys are rejected. Missing,
extra, reordered, duplicated or altered parts cannot be treated as complete.
Success reports PinnedBytesVerified but keeps complete archive Unknown and
native execution NotRun: this tool checks one stored artifact, not the other
archive members or the build's meaning. In-memory fixture APIs accept explicit
test targets; the command-line interface stays pinned to the real target.

Hash agreement is relative integrity, not authentication. The tool makes no
claim of a safe native binary, safe arbitrary filesystem service or resistance
to a concurrently hostile filesystem. The documented shell timeout is the hard
time bound. Core allocation is bounded by encoded-byte limits; measured process
RSS is separately reported and is not inferred from file sizes.

## Finite calibration and handoff

```sh
timeout 5s python3 symbol-surface/transport-v0/check_transport.py
```

Two deterministic gzip fixtures exercise distinct four-part and six-part
transfers. Both are verified in memory and through serialized filesystem
records. Twenty-two refusal controls cover missing/extra files and parts,
duplicate/reordered manifest entries, altered bytes, invalid base64 even after
repinning that part, the wrong independently expected output, resource bounds,
duplicate JSON keys and refusal to package a synthetic fixture as the real
artifact. `report.json` retains actual phase costs and Linux peak RSS.

This advances an engineering interface, with no new mathematical word, theorem,
learning or acceleration claim. The original nine obligations stay Open.
It gives the producing agent a concrete command to supply the missing bytes
and the receiving agent an executable acceptance boundary. Actual usefulness
for Jiamin's task has not been measured.

Next: the producer may publish the real package in response to the existing
cross-linked PR. Once received, check its byte pin, then separately replay the
full archive verifier. No automatic polling, merge or native execution follows.

## Transfer-to-archive handoff

The peer's existing `experiments/advance_symbol_surface/verify_evidence.py`
already bounds gzip reads to 64 MiB plus one sentinel byte and compares the
original length/digest against the retained report. Its source was inspected
at Adva `e0e3433`; it is not reimplemented here. The missing interface was that
the original transport `verify` discarded the recovered stored bytes.

The additional `restore` command validates the entire transfer first, creates
one fresh output with exclusive creation, flushes and syncs its contents, then
reads back and verifies the stored bytes. It performs no decompression or native
execution. Only the frozen real target is accepted by the CLI.

```sh
timeout 5s python3 symbol-surface/transport-v0/transport.py restore /path/to/received-text-parts /path/to/evidence/run-01/_native.abi3.so.gz
```

The destination's parent must already exist and the destination must be absent.
An existing file or symlink is rejected, even when its bytes would match.
Validation failure creates no output. An interruption, disk-full or write error
after creation may leave a partial file; that is not a success receipt. The tool
does not overwrite or automatically delete it. File sync and readback do not
constitute a crash-atomic publication or an authenticated artifact.

After a successful real restoration, the separate full archive check is:

```sh
timeout 10s python3 /path/to/adva/experiments/advance_symbol_surface/verify_evidence.py --evidence /path/to/evidence/run-01
```

This requires all 54 exact archive files. A restore success alone leaves
complete archive Unknown and native replay NotRun. The full verifier was only
inspected in this round; it cannot run to completion without the real artifact.

Frozen calibration: two synthetic gzip payloads, seven refusal controls,
five seconds total, no search and no native calls. The first payload is a
short string; the reuse payload is 262,144 bytes. The independent fixture
gzip reader is capped at 262,145 output bytes. Controls cover an existing
destination, modified input, attempted promotion to the real target and a
symlink destination. Crash/disk-full fault injection is outside this run.

```sh
timeout 5s python3 symbol-surface/transport-v0/check_restore.py
```

`restore-report.json` records the bounded run. Its result is synthetic filesystem
handoff evidence, not real artifact reception. The previous transfer-only
report and historical receiving acknowledgment remain unchanged. This small
addition lets the receiver hand checked stored bytes to the existing archive
verifier without manually inventing another decoding script.
