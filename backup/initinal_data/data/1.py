from json import load, dump, loads
from pprint import pprint

p = set()
with open('list') as f:
    list = [i.strip() for i in f.read().split()]
for j in list:
    with open(j) as f:
    	s = load(f)
    for i in range(len(s)):
        if 'uid' in s[i]['properties']: s[i]['properties'].pop('uid')
    dump(s, open(j, 'w', encoding='utf-8'), indent=4, sort_keys=True, ensure_ascii=False)
