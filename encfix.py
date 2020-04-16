#!/usr/bin/env python3

""" EncFix: Guess and fix character encodings of garbled filenames

    Copyright (C) 2020 Arnie97 <arnie97@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""


import argparse
import chardet
import itertools
import os
import re
import unicodedata
import urllib.parse


CHARSETS = [
    'latin-1',
    'cp1251',
    'cp1252',
    'mac-roman',
    'iso2022-jp',
    'mbcs',
    'euc-kr',
    'shift-jis',
    'big5',
    'gbk',
    'utf-8',
]


def recover_raw_data(s: str) -> bytes:
    if re.search('%[0-9A-F]{2}', s, re.IGNORECASE):
        return urllib.parse.unquote_to_bytes(s)

    s = unicodedata.normalize('NFC', s)
    for charset in CHARSETS:
        try:
            raw = s.encode(charset)
        except (UnicodeEncodeError, LookupError):
            pass
        else:
            return raw


def fix_encoding(s: str) -> str:
    raw = recover_raw_data(s)
    detected_charset = chardet.detect(raw)['encoding']
    detected_charset = [detected_charset] if detected_charset else []

    for charset in itertools.chain(detected_charset, reversed(CHARSETS)):
        try:
            fixed = raw.decode(charset)
            assert s != fixed
        except (UnicodeDecodeError, LookupError, AssertionError):
            pass
        else:
            return fixed
    return s


def main() -> None:
    parser = argparse.ArgumentParser(description='Guess and fix character encodings of garbled filenames.')
    parser.add_argument('-f', '--force', action='store_true', help='overwrite existing files; without this flag, the default behavior is to skip them')
    parser.add_argument('-q', '--quiet', action='store_true', help='do not print what is being done')
    parser.add_argument('-n', '--dry-run', action='store_true', help='do not rename the files, just show what would have been done')
    parser.add_argument('-v', '--verbose', action='store_true', help='also print untouched files')
    parser.add_argument('files', nargs='+', metavar='FILE', help="file with garbled name")
    args = parser.parse_args()

    for path in args.files:
        directory, name = os.path.split(path)
        new_name = fix_encoding(name)
        if name == new_name:
            if args.verbose and not args.quiet:
                print(name, '?')
            continue

        new_path = os.path.join(directory, new_name)
        if args.force or not os.path.exists(new_path):
            if not args.quiet:
                print(name, '->', new_name)
            if not args.dry_run:
                os.rename(path, new_path)
        elif args.verbose and not args.quiet:
            print(name, '!>', new_name)


if __name__ == '__main__':
    main()
