#!/usr/bin/env python3

# Usage: ./rewrite_json.py g2p-mapping.json > compact-g2p-mapping.json
# Requirements: pip install g2p

import io
import json
import sys

from g2p.mappings.utils import CompactJSONMappingEncoder

# We always want utf-8, darn it, even when Windows doesn't think so.
if sys.stdout.encoding != "utf8" and hasattr(sys.stdout, "buffer") and "pytest" not in sys.modules:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf8")

with open(sys.argv[1], encoding="utf8") as f:
    data = json.load(f)

json.dump(data, sys.stdout, indent=4, ensure_ascii=False, cls=CompactJSONMappingEncoder)
