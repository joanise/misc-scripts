#!/usr/bin/env python3

import unicodedata as ud
import sys
sys.stdout.reconfigure(encoding="utf8")

infile = sys.argv[1]
with open(infile, encoding="utf8") as f:
    for line in f:
        print(ud.normalize("NFC", line), end="")
