#!/usr/bin/env python3
"""Original ChatGPT (OpenAI) contribution under Unknown v0.3. Offline only."""
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent
# Independently selected implementation bytes, never obtained from the manifest.
EXPECTED = {'manifest.schema.json': 'e71fb10f9d33c3fe732e170e9b91f65c3464af6b97b020e607801268910d79a3', 'check_manifest.py': '96183069b7f23db24a83f8983292c73ab64ea86cf8cf103ca6f0f039ef0574e3', 'lookup_reference.py': '3049fe81ae1f07877f4005080407073ce01c437d5a465611dd7932f78629cbf4', 'README.md': '459e436e0625f76f0917063335a80f70f62779e61600a118e30ab4c3aa2971d2', 'package-capabilities-v0.1-proposal.md': 'd37b164f14d188847f0a67167f805f30c75b8e278e8faa056c61ddf7563fa3f3', 'kernel-package-boundary-v0.1.md': '6e88fa6ab69887d6429a12796a99445a6e4d54a0618a5a9872bd0531e66d609f'}


def load_receiver():
    for name, digest in EXPECTED.items():
        if hashlib.sha256((ROOT/'machine'/name).read_bytes()).hexdigest() != digest:
            raise ValueError('Machine implementation byte mismatch: '+name)
    for name in ('check_manifest', 'lookup_reference'):
        spec = importlib.util.spec_from_file_location(name, ROOT/'machine'/(name+'.py'))
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules['check_manifest'], sys.modules['lookup_reference']


def check(manifest, checkout, commit, digests, seconds=10.0):
    start = time.monotonic()
    result = dict(status='Unknown', reason_code='Unavailable', references_checked=0,
                  semantic_verification='NotRun', native_admission='NotGranted',
                  native_launches=0, residuals=['Local repository label is caller-bound, not authenticated.',
                  'Documentary lookup does not establish truth, rights or completed KPB-14 adoption.'])
    try:
        if not math.isfinite(seconds) or seconds <= 0:
            result['reason_code'] = 'BudgetExhausted'
            return result
        lint, receiver = load_receiver()
        metadata = lint.lint(manifest, deadline_seconds=seconds-(time.monotonic()-start))
        if metadata['status'] != 'MetadataConsistent':
            result.update(status=metadata['status'], reason_code='MetadataNotAccepted', metadata=metadata)
            return result
        account = dict(bytes_read=0, parse_calls=0, visited_values=0)
        data = lint.parse(lint.bounded_read(manifest, account), account)
        expected = lint.parse(lint.bounded_read(digests, account), account)
        if not isinstance(expected, list) or len(expected)>256:
            raise ValueError('Digest inventory must be a bounded list')
        pins = {}
        for item in expected:
            if not isinstance(item, dict) or set(item)!={'repository','commit','path','sha256'}:
                raise ValueError('Unsupported digest inventory shape')
            key = tuple(item[k] for k in ('repository','commit','path'))
            if key in pins:
                raise ValueError('Duplicate digest inventory coordinate')
            pins[key] = item['sha256']
        sources = []
        for node in data['content']:
            if not node['sources']:
                result.update(status='Rejected', reason_code='MissingSource')
                return result
            sources.extend(node['sources'])
        if not data['provenance']['sources']:
            result.update(status='Rejected', reason_code='MissingSource')
            return result
        sources.extend(data['provenance']['sources'])
        # The source-contract is checked against the separately pinned machine bytes.
        contract = data['capabilities'][0]['source_contract']
        if contract != {'repository':'mountain/adva-machine', 'commit':'089c5ab8ec5f04768d03a377d0180e942fd77216', 'path':'spec/framework/kernel-package-boundary-v0.1.md'}:
            result.update(status='Rejected', reason_code='IncompatibleSourceContract')
            return result
        seen = set()
        with tempfile.TemporaryDirectory() as temp:
            refpath = Path(temp)/'reference.json'
            for source in sources:
                key = tuple(source[k] for k in ('repository','commit','path'))
                if key in seen:
                    continue
                seen.add(key)
                if key not in pins:
                    result.update(status='Rejected', reason_code='MissingDigestPin')
                    return result
                remaining = seconds-(time.monotonic()-start)
                if remaining <= 0:
                    result['reason_code'] = 'BudgetExhausted'
                    return result
                refpath.write_text(json.dumps(dict(source, sha256=pins[key])))
                found = receiver.lookup(refpath, 'mountain/adva-library', commit, checkout, seconds=remaining)
                result['references_checked'] += 1
                if found['status'] != 'ReferenceBytesLocated':
                    result.update(status=found['status'], reason_code=found['reason_code'], reference_result=found)
                    return result
        result.update(status='ReferenceBytesLocated', reason_code='Located', metadata_status=metadata['status'],
                      ignored_optional_extensions=metadata['ignored_optional_extensions'])
    except (sys.modules['check_manifest'].Exhausted if 'check_manifest' in sys.modules else TimeoutError) as error:
        result.update(reason_code='BudgetExhausted', reason=str(error)[:256])
    except (sys.modules['check_manifest'].Refusal if 'check_manifest' in sys.modules else RuntimeError) as error:
        result.update(status='Rejected', reason_code='InvalidInput', reason=str(error)[:256])
    except (ValueError, KeyError, TypeError, UnicodeError, RecursionError) as error:
        result.update(status='Rejected', reason_code='InvalidInput', reason=str(error)[:256])
    except (OSError, ImportError) as error:
        result.update(reason=str(error)[:256])
    finally:
        result['elapsed_seconds'] = time.monotonic()-start
        if result['elapsed_seconds'] > seconds:
            result.update(status='Unknown', reason_code='BudgetExhausted')
    return result


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--manifest', type=Path, default=ROOT/'manifest.json')
    p.add_argument('--digests', type=Path, default=ROOT/'source-digests.json')
    p.add_argument('--checkout', type=Path, required=True)
    p.add_argument('--commit', required=True, help='Independently selected full library consumer pin')
    p.add_argument('--seconds', type=float, default=10.0)
    args = p.parse_args()
    r = check(args.manifest, args.checkout, args.commit, args.digests, args.seconds)
    print(json.dumps(r, sort_keys=True, allow_nan=False))
    sys.exit(0 if r['status']=='ReferenceBytesLocated' else 2 if r['status']=='Rejected' else 3)
