"""Original finite controls, ChatGPT (OpenAI), Unknown v0.3."""
import copy
import json
from pathlib import Path
import tempfile
import subprocess
import sys
import unittest
from unittest.mock import patch
from check_references import check, load_receiver, ROOT

BASE = '19cede9c4532b7abd85f200daf7a9611a84563f0'
CHECKOUT = ROOT.parents[1]


class Controls(unittest.TestCase):
    def run_case(self, mutate=None, commit=BASE, seconds=10, digests=None):
        data = json.loads((ROOT/'manifest.json').read_text())
        if mutate:
            mutate(data)
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp)/'manifest.json'
            p.write_text(json.dumps(data))
            d = ROOT/'source-digests.json'
            if digests is not None:
                d = Path(temp)/'digests.json'
                d.write_text(json.dumps(digests))
            return check(p, CHECKOUT, commit, d, seconds)

    def test_missing_dependency_returns_unknown(self):
        # A clean interpreter without site packages cannot import jsonschema.
        r = subprocess.run([sys.executable, '-S', str(ROOT/'check_references.py'),
                            '--checkout', str(CHECKOUT), '--commit', BASE],
                           capture_output=True, text=True, timeout=30)
        self.assertEqual(r.returncode, 3, r.stderr)
        report = json.loads(r.stdout)
        self.assertEqual((report['status'], report['reason_code']), ('Unknown', 'Unavailable'))
        self.assertEqual((report['native_launches'], report['semantic_verification'],
                          report['native_admission']), (0, 'NotRun', 'NotGranted'))
        self.assertNotIn('Traceback', r.stderr)

    def test_real_sources(self):
        r = self.run_case()
        self.assertEqual(r['status'], 'ReferenceBytesLocated')
        self.assertEqual(r['references_checked'], 3)
        self.assertEqual((r['native_launches'], r['semantic_verification'], r['native_admission']), (0,'NotRun','NotGranted'))

    def test_missing_source(self):
        r = self.run_case(lambda x:x['content'][0].update(sources=[]))
        self.assertEqual(r['reason_code'], 'MissingSource')

    def test_missing_local_bytes(self):
        d = json.loads((ROOT/'source-digests.json').read_text())
        d[0]['path'] = 'absent-original.md'
        r = self.run_case(lambda x:x['content'][0]['sources'][0].update(path='absent-original.md'), digests=d)
        self.assertEqual((r['status'],r['reason_code']), ('Unknown','Unavailable'))

    def test_revision_mismatch(self):
        r = self.run_case(commit='0'*40)
        self.assertEqual(r['reason_code'], 'IncompatibleRevision')

    def test_digest_mismatch(self):
        d = json.loads((ROOT/'source-digests.json').read_text()); d[0]['sha256']='0'*64
        self.assertEqual(self.run_case(digests=d)['reason_code'],'IncompatibleDigest')

    def test_required_unknown_extension(self):
        r=self.run_case(lambda x:x['extensions'].append(dict(namespace='unknown/view',version='0',required=True,data={})))
        self.assertEqual(r['status'],'Unknown')

    def test_optional_unknown_extension(self):
        r=self.run_case(lambda x:x['extensions'].append(dict(namespace='unknown/view',version='0',required=False,data={})))
        self.assertEqual(r['status'],'ReferenceBytesLocated')
        self.assertEqual(r['ignored_optional_extensions'],['unknown/view'])

    def test_budget(self):
        self.assertEqual(self.run_case(seconds=0)['reason_code'],'BudgetExhausted')

    def test_computation_and_premise_are_not_references(self):
        for kind in ('computation-dependency','proof-premise'):
            with self.subTest(kind=kind):
                self.assertEqual(self.run_case(lambda x:x['relations'][0].update(kind=kind))['status'],'Rejected')

    def test_no_pin_inference(self):
        d=json.loads((ROOT/'source-digests.json').read_text()); d.pop(0)
        self.assertEqual(self.run_case(digests=d)['reason_code'],'MissingDigestPin')

    def test_machine_tamper_before_import(self):
        with patch('check_references.EXPECTED', {'check_manifest.py':'0'*64}):
            with self.assertRaises(ValueError):
                load_receiver()

    def test_dangling_trail(self):
        self.assertEqual(self.run_case(lambda x:x['trails'][0]['steps'].append('missing'))['status'],'Rejected')

    def test_source_contract_mismatch(self):
        r=self.run_case(lambda x:x['capabilities'][0]['source_contract'].update(commit='0'*40))
        self.assertEqual(r['reason_code'],'IncompatibleSourceContract')

    def test_duplicate_digest_fields(self):
        with tempfile.TemporaryDirectory() as temp:
            d=Path(temp)/'digests.json'
            d.write_text('[{"repository":"x/y","repository":"x/y"}]')
            r=check(ROOT/'manifest.json', CHECKOUT, BASE, d)
            self.assertEqual(r['status'],'Rejected')

    def test_oversized_manifest(self):
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp)/'manifest.json'; p.write_bytes(b' '*65537)
            r=check(p, CHECKOUT, BASE, ROOT/'source-digests.json')
            self.assertEqual(r['status'],'Unknown')

if __name__=='__main__':
    unittest.main()
