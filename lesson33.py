l = (1, 2, 3, 4, 5)
r = []

for i in l:
    # r.append(i)
    if i % 2 == 0:
        r.append(i)

print(r)

# r = [i for i in l]
r = [i for i in l if i % 2 == 0]
print(r)