#!/usr/bin/env python3
"""Finite text transport of pinned bytes. No decompression or native execution."""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import re

PART = 65536
MAX_PARTS = 64
MAX_TEXT = 4 * 1024 * 1024
MAX_RAW = MAX_TEXT // 4 * 3
TARGET = {
    'repository': 'mountain/adva',
    'commit': 'e0e3433ebcaa2da6ec3e0bc1f67bd316f2c38547',
    'path': 'experiments/advance_symbol_surface/evidence/run-01/_native.abi3.so.gz',
    'bytes': 2039917,
    'sha256': 'f31edc374020672cba9c783be8898243a33653b6548b9f25754db82c9302b423',
}


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def bounded_read(path, limit):
    require(not path.is_symlink() and path.is_file(), 'not a regular non-symlink file')
    with path.open('rb') as stream:
        raw = stream.read(limit + 1)
    require(len(raw) <= limit, 'file byte budget exceeded')
    return raw


def check_target(target):
    require(type(target['bytes']) is int and 0 < target['bytes'] <= MAX_RAW, 'raw byte budget')
    require(isinstance(target['sha256'], str) and
            re.fullmatch('[0-9a-f]{64}', target['sha256']), 'invalid target digest')


def encode(raw, target):
    check_target(target)
    require(len(raw) == target['bytes'] and sha(raw) == target['sha256'], 'input target mismatch')
    text = base64.b64encode(raw)
    require(len(text) <= MAX_TEXT, 'text byte budget')
    chunks = [(f'part-{i // PART:03d}.b64', text[i:i + PART])
              for i in range(0, len(text), PART)]
    manifest = {'schema': 'adva.pinned-byte-text-transport.proposed', 'version': 0,
                'target': target, 'encoded_bytes': len(text),
                'parts': [{'name': name, 'bytes': len(data), 'sha256': sha(data)}
                          for name, data in chunks]}
    return manifest, dict(chunks)


def validate_manifest(manifest, expected):
    check_target(expected)
    require(manifest['schema'] == 'adva.pinned-byte-text-transport.proposed' and
            type(manifest['version']) is int and manifest['version'] == 0, 'schema/version')
    require(manifest['target'] == expected, 'manifest target mismatch')
    parts = manifest['parts']
    require(isinstance(parts, list) and 1 <= len(parts) <= MAX_PARTS, 'part count budget')
    count = (4 * ((expected['bytes'] + 2) // 3) + PART - 1) // PART
    require(len(parts) == count, 'noncanonical part count')
    require([p['name'] for p in parts] == [f'part-{i:03d}.b64' for i in range(count)],
            'part order, duplicate or name mismatch')
    encoded = 4 * ((expected['bytes'] + 2) // 3)
    require(type(manifest['encoded_bytes']) is int and manifest['encoded_bytes'] == encoded
            and encoded <= MAX_TEXT, 'encoded byte budget')
    for i, p in enumerate(parts):
        require(type(p['bytes']) is int and p['bytes'] == min(PART, encoded - i * PART),
                'part size mismatch')
        require(isinstance(p['sha256'], str) and re.fullmatch('[0-9a-f]{64}', p['sha256']),
                'invalid part digest')
    return parts


def decode(manifest, chunks, expected):
    parts = validate_manifest(manifest, expected)
    require(set(chunks) == {p['name'] for p in parts}, 'missing or extra part')
    ordered = []
    for p in parts:
        data = chunks[p['name']]
        require(len(data) == p['bytes'] and sha(data) == p['sha256'], 'part bytes mismatch')
        ordered.append(data)
    text = b''.join(ordered)
    raw = base64.b64decode(text, validate=True)
    require(base64.b64encode(raw) == text, 'noncanonical base64')
    require(len(raw) == expected['bytes'] and sha(raw) == expected['sha256'], 'decoded target mismatch')
    return raw


def no_duplicate_keys(pairs):
    out = {}
    for key, value in pairs:
        require(key not in out, 'duplicate JSON key')
        out[key] = value
    return out


def receive(directory, expected):
    manifest = json.loads(bounded_read(directory / 'manifest.json', 32768),
                          object_pairs_hook=no_duplicate_keys)
    parts = validate_manifest(manifest, expected)
    expected_files = {'manifest.json'} | {p['name'] for p in parts}
    # Bounded enumeration rejects oversized directories without materializing them.
    names = set()
    for entry in directory.iterdir():
        require(len(names) < MAX_PARTS + 1, 'directory entry budget')
        names.add(entry.name)
    require(names == expected_files, 'missing or extra transport file')
    chunks = {p['name']: bounded_read(directory / p['name'], p['bytes']) for p in parts}
    return decode(manifest, chunks, expected)


def restore(directory, output, expected):
    """Validate first, then create one fresh stored artifact, without executing it.

    An interrupted write can leave an incomplete file. This operation never
    treats such a file as verified, overwrites it, or silently removes it.
    """
    raw = receive(directory, expected)
    with output.open('xb') as stream:
        written = stream.write(raw)
        require(written == len(raw), 'incomplete output write')
        stream.flush()
        os.fsync(stream.fileno())
    retained = bounded_read(output, expected['bytes'])
    require(len(retained) == expected['bytes'] and sha(retained) == expected['sha256'],
            'stored output mismatch')
    return {'status': 'PinnedStoredBytesRestored', 'bytes': len(retained),
            'sha256': sha(retained), 'complete_archive_status': 'Unknown',
            'native_execution': 'NotRun', 'decompression': 'NotRun'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    pack = sub.add_parser('pack', help='producer: package the exact frozen native gzip')
    pack.add_argument('input', type=Path)
    pack.add_argument('output', type=Path)
    verify = sub.add_parser('verify', help='receiver: verify only, write or execute nothing')
    verify.add_argument('directory', type=Path)
    materialize = sub.add_parser('restore', help='verify then create one fresh gzip file; no execution')
    materialize.add_argument('directory', type=Path)
    materialize.add_argument('output', type=Path)
    args = parser.parse_args()
    if args.command == 'pack':
        manifest, chunks = encode(bounded_read(args.input, TARGET['bytes']), TARGET)
        args.output.mkdir(exist_ok=False)
        for name, data in chunks.items():
            (args.output / name).write_bytes(data)
        (args.output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
        print(json.dumps({'status': 'PinnedBytesPackaged', 'parts': len(chunks),
                          'target': TARGET, 'native_execution': 'NotRun'}))
    elif args.command == 'restore':
        print(json.dumps(restore(args.directory, args.output, TARGET)))
    else:
        raw = receive(args.directory, TARGET)
        print(json.dumps({'status': 'PinnedBytesVerified', 'bytes': len(raw),
                          'sha256': sha(raw), 'complete_archive_status': 'Unknown',
                          'native_execution': 'NotRun', 'decompression': 'NotRun'}))


if __name__ == '__main__':
    main()
