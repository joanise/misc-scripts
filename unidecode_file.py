#!/usr/bin/env python3

# Usage: ./unidecode_file.py < input_with_utf8_escapes > output_in_true_utf8
# Requirements: pip install g2p

import io
import sys
from g2p.mappings.utils import unicode_escape

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf8")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf8")

for line in sys.stdin:
    # print("in:", len(line), line, end="")
    # print("out:", len(unicode_escape(line)), unicode_escape(line), end="")
    print(unicode_escape(line), end="")
