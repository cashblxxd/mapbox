from json import load, dump, loads
from pprint import pprint
import os
from sys import exit


with open('main.json') as f:
    for i in load(f): print(i)

'''j = 0
index = {}
main = {}
try:
    for root, dirs, files in os.walk(".", topdown=False):
       for name in files:
           if root in ('./dist_data', './data') and name.endswith('.json') and name != 'problems.json':
               with open(os.path.join(root, name)) as f:
                   k = name.rstrip('.json')
                   s = load(f)
                   for i in range(len(s)):
                       j += 1
                       s[i]["properties"]["id"] = j
                       index[j] = {"collection": k, "index": i}
                   main[k] = {"features": s}
               #dump(s, open(os.path.join(root, name), 'w+', encoding='utf-8'), indent=4, sort_keys=True, ensure_ascii=False)
except Exception as e:
    print(os.path.join(root, name))
    print(e)
    print(s)
    print(i)
    print(s[i])
dump(main, open('main.json', 'w', encoding='utf-8'), indent=4, sort_keys=True, ensure_ascii=False)
dump(index, open('index.json', 'w', encoding='utf-8'), indent=4, sort_keys=True, ensure_ascii=False)
       #if name.startswith('./dist_data/') or name.startswith('./data/'):

with open('nr.json') as f:
	s = load(f)
	for i in range(len(s)):
		for j in s[i]['properties']:
			if isinstance(s[i]['properties'][j], str): s[i]['properties'][j] = '»'.join(s[i]['properties'][j].replace('"', '«').rsplit('«', 1))
dump(s, open('nr1.json', 'w', encoding='utf-8'), indent=4, sort_keys=True, ensure_ascii=False)
'''
