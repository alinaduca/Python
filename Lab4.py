import json
import functools

d = {
    'k1' : 19,
    'k2' : 9.0,
    'k3' : 'Hello',
    'k4' : (1, 3, 5, 7, 9),
    'k5' : [89, 4.0, "abc"],
    'k6' : {
        'k11' : 'a',
        'k22' : ['1', '2', '3']
    }
}

print(d)

print(d.keys())
print(d.values())

for i, (k, v) in enumerate(d.items()):
    print(k, v)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
u = [x + 5 for x in l]
p = list(map(lambda x : x+5, l))

print(l)
print(p)
print(u)

q = functools.reduce(lambda x,y : x+y, l)
print(q)

l1 = [10, 11, 12, 13, 14]
l2 = ['abc', 'def', 'ghi', 'xyz']
z = list(zip(l1, l2))
print(z)
for el in z:
    print(el[0], el[1])

t = "".join(['1', '11', '111'])
print(t)

with open('fisier.json', 'w') as f:
    json.dump(d, f)

with open('fisier.json', 'r') as f:
    d = json.load(f)