"""Proposed documentary endpoint swap. Never evaluates the archived mathematics."""
import argparse
import copy
import hashlib
import json
import resource
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FILES = ["README.md", "construct_records.py", "inspect_representation.py", "inspection.json",
         "presentation.json", "contract.json", "obligations.json", "symbol-surface.adva"]
COMMIT = "6538f98555db89f0569aed39952d355bc10c0cd0"


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def read(path):
    with path.open("rb") as stream:
        data = stream.read(65537)
    require(len(data) <= 65536, "per-file byte budget")
    return data


def swap(document):
    require(document["schema"] == "adva.symbol-surface.endpoint-swap.proposed", "schema")
    require(document["orientation"] in ["record-to-name", "name-to-record"], "orientation")
    require(len(document["rows"]) <= 16, "row budget")
    require(all(row["status"] == "DeclaredNotExecuted" for row in document["rows"]), "status promotion refused")
    result = copy.deepcopy(document)
    for row in result["rows"]:
        row["left"], row["right"] = row["right"], row["left"]
    result["orientation"] = {"record-to-name": "name-to-record", "name-to-record": "record-to-name"}[document["orientation"]]
    return result


def construct():
    raw = {name: read(ROOT / "source" / name) for name in FILES}
    p = json.loads(raw["presentation.json"])
    o = json.loads(raw["obligations.json"])
    require(len(o["items"]) == 9 and all(x["status"] == "Open" for x in o["items"]), "source obligations")
    rows = []
    for index, symbol in enumerate(p["symbols"]):
        pointer, residual = {
            "imaginary-unit": ("/symbols/0", "Only an atom declaration; no construction witness supplied"),
            "pi": ("/pi_record", "Five equation strings; branch and division checks not replayed"),
            "negative-one": ("/result_claim", "Hole filling and typed equality not natively replayed"),
        }[symbol["id"]]
        rows.append({"id": "relation-" + str(index),
                     "left": {"kind": "document-record", "file": "source/presentation.json", "pointer": pointer},
                     "right": {"kind": "symbol-name", "id": symbol["id"], "type": symbol["mathematical_type"]},
                     "address_code": symbol["address_code"], "status": "DeclaredNotExecuted", "residual": residual})
    return {"schema": "adva.symbol-surface.endpoint-swap.proposed", "version": 0,
            "orientation": "record-to-name", "rows": rows,
            "source": {"repository": "mountain/adva", "pull_request": 170, "commit": COMMIT,
                       "status_at_capture": "Open draft; not merged",
                       "files": [{"path": "experiments/symbol_surface/" + name,
                                  "archive": "source/" + name,
                                  "sha256": hashlib.sha256(raw[name]).hexdigest()} for name in FILES]},
            "preserved": {"obligations": o["items"], "full_content": "Eight unchanged source files retained",
                          "native_load": "NotRun", "native_admission": "not-granted",
                          "arithmetic_evaluation": "NotRun", "game_execution": "NotRun"},
            "scope": "Swap two documentary endpoint coordinates, retaining the third relation record. Not a native swap, conjugation, inverse function, D-star or proof transport."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write the two proposed views; no proof execution")
    args = parser.parse_args()
    start = time.perf_counter_ns()
    forward = construct()
    reverse = swap(forward)
    require(swap(reverse) == forward, "round trip")
    if args.write:
        (ROOT / "record-to-name.json").write_bytes(encode(forward))
        (ROOT / "name-to-record.json").write_bytes(encode(reverse))
    else:
        require(read(ROOT / "record-to-name.json") == encode(forward), "forward drift")
        require(read(ROOT / "name-to-record.json") == encode(reverse), "reverse drift or source drift")
    # Reuse control: two retained documentary records can name the same symbol.
    control = copy.deepcopy(forward)
    extra = copy.deepcopy(control["rows"][-1])
    extra["id"] = "synthetic-alternative"
    extra["left"] = {"kind": "synthetic-record", "label": "different construction; not added to source"}
    control["rows"].append(extra)
    changed = swap(control)
    require(len([r for r in changed["rows"] if r["left"].get("id") == "negative-one"]) == 2, "alternative lost")
    require(swap(changed) == control, "control round trip")
    bad = copy.deepcopy(forward)
    bad["rows"][0]["status"] = "Proved"
    try:
        swap(bad)
    except ValueError:
        pass
    else:
        raise ValueError("promotion control accepted")
    report = {"status": "DocumentarySwapChecked", "source_commit": COMMIT,
              "rows": 3, "source_files_retained": 8, "open_obligations": 9,
              "controls": {"double_swap": "Pass", "nonunique_reverse_preserved": "Pass", "status_promotion_rejected": "Pass"},
              "arithmetic_evaluations": 0, "native_operations": 0, "game_moves": 0,
              "elapsed_ms_before_report_serialization": (time.perf_counter_ns() - start) / 1e6,
              "process_peak_rss_kib_linux": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              "unmeasured": ["research", "network", "initial document construction", "report serialization"],
              "boundary": "Checks this finite documentary transformation, not mathematical truth, native identity, origin authentication or universal faithfulness"}
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
