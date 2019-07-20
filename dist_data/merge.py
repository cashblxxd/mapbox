from json import load, dump, loads

a = {}
with open('houses.json') as f:
    s = load(f)
    lens = len(s)
    for i in range(len(s)):
        a[s[i]["properties"]["address"]] = s[i]
x = 0
with open('all_houses.json') as f:
    s = load(f)
    for i in range(len(s)):
        if s[i]["properties"]["address"] in a:
            a[s[i]["properties"]["address"]]["properties"] = {**a[s[i]["properties"]["address"]]["properties"], **s[i]["properties"]}
            x += 1
        else:
            a[s[i]["properties"]["address"]] = s[i]
    print(x, len(s), lens, len(s) + lens)
    print(x / (len(s) + lens) * 100, '%')
b = []
for i in a:
    b.append(a[i])
dump(b, open('new.json', 'w', encoding='utf-8'), indent=4, sort_keys=True, ensure_ascii=False)
