l = (1, 2, 3, 4, 5)
l2 = (5, 6, 7, 8, 9, 10)
r = []

for i in l:
    # r.append(i)
    if i % 2 == 0:
        r.append(i)

print(r)

# r = [i for i in l]
r = [i for i in l if i % 2 == 0]
print(r)

r = []
for i in l:
    for j in l2:
        r.append(i * j)

print(r)