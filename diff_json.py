import json
import sys

with open(sys.argv[1], encoding="utf8") as f:
    data1 = json.load(f)
with open(sys.argv[2], encoding="utf8") as f:
    data2 = json.load(f)
if data1 == data2:
    print("Files JSON-identical")
else:
    print("FILES non JSON-identical")
