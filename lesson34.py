w = ["mon", "tue", "wed"]
f = ["coffee", "milk", "water"]

# d = {}
# for k, v in zip(w, f):
#     d[k] = v

# print(d)

# d = {x: y for x, y in zip(w, f)}
# print(d)

s = set()
for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)