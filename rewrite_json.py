#!/usr/bin/env python3

# Usage: ./rewrite_json.py g2p-mapping.json > compact-g2p-mapping.json
# Requirements: pip install g2p

import json
import sys

from g2p.mappings.utils import CompactJSONMappingEncoder

with open(sys.argv[1], encoding="utf8") as f:
    data = json.load(f)
json.dump(data, sys.stdout, indent=4, ensure_ascii=False, cls=CompactJSONMappingEncoder)
