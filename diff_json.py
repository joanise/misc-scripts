import json
import sys

def same_modulo_order(data1, data2):
    try:
        return ordered(data1, key=json.dumps) == ordered(data2, key=json.dumps)
    except:
        return False

with open(sys.argv[1], encoding="utf8") as f:
    data1 = json.load(f)
with open(sys.argv[2], encoding="utf8") as f:
    data2 = json.load(f)
if data1 == data2:
    print("Files JSON-identical")
elif same_modulo_order(data1, data2):
    print("Files have the same contents in a different order.")
else:
    print("FILES non JSON-identical")

# Alternative commands using jq, recommended by Samuel Larkin:
# sha1sum  <(jq --sort-keys . file1.json) <(jq --sort-keys . file2.json)
# diff <(jq --sort-keys . file1.json) <(jq --sort-keys . file2.json)
# vimdiff <(jq --sort-keys . file1.json) <(jq --sort-keys . file2.json)
# or, maybe you just want to compare the "source" elements:
# vimdiff <(jq --sort-keys .source file1.json)  <(jq --sort-keys .source file2.json)
