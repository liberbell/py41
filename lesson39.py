# print(globals())

# builtins.print()

ranking = {
    "A": 100,
    "B": 85,
    "C": 90
}

for key in ranking:
    print(key)

print(sorted(ranking, key=ranking.get, reverse=True))

s = "aoekkdergkxsptyqqvgjsffs"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1

print(d)

d = {}
for c in s:
    c.setdefault(c, 0)
    d[c] += 1

print(d)