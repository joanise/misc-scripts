#!/usr/bin/env python3

import unicodedata as ud
import sys
sys.stdout.reconfigure(encoding="utf8")

if len(sys.argv) > 1:
    infile = sys.argv[1]
    with open(infile, encoding="utf8") as f:
        for line in f:
            print(ud.normalize("NFD", line), end="")
else:
    sys.stdin.reconfigure(encoding="utf8")
    for line in sys.stdin:
        print(ud.normalize("NFD", line), end="")
