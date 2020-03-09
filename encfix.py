#!/usr/bin/env python3

import chardet
import os
import sys
import unicodedata
import urllib.parse


def recover_raw_data(s: str) -> bytes:
    if '%' in s:
        return urllib.parse.unquote_to_bytes(s)

    s = unicodedata.normalize('NFC', s)
    for charset in ['latin-1', 'cp1251', 'cp1252', 'mac-roman', 'mbcs', 'gbk', 'big5', 'shift-jis', 'utf-8']:
        try:
            raw = s.encode(charset)
        except:
            pass
        else:
            return raw


def fix_encoding(s: str) -> str:
    raw = recover_raw_data(s)
    return raw.decode(chardet.detect(raw)['encoding'])


if __name__ == '__main__':
    for path in sys.argv[1:]:
        directory, name = os.path.split(path)
        new_name = fix_encoding(name)
        if name == new_name:
            print(name, '?')
            continue
        print(name, '->', new_name)
        os.rename(path, os.path.join(directory, new_name))
