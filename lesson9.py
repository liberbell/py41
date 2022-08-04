r = [1, 2, 3, 4, 5, 6, 7, 8, 1, 5, 6]
print(r.index(5, 5))

print(r.count(6))

if 10 in r:
    print("exist!")

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)