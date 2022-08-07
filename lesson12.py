t = (1, 2, 3, 4, 5)
print(t)
print(type(t))
print(t[1])
print(t.index(3))

t = ([1, 2, 3], [4, 5, 6])
# t[0] = 1
t[0][0] = 10
print(t)

new_tuple = (1, 2, 3) + (4, 5, 6)
print(new_tuple)

num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

min, max = 0, 100
print(min, max)
a, b, c, d, e, f = "Mike", "1", 1, "1", "e", "f"
print(a, b, c, d, e, f)