from operator import le


l = [1, 20, 12, 4, 5, 8]
# print(l[0])
# print(type(l))
# print(len(l))
# print(list("abcdefg"))

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(n[::2])
# print(n[::-1])

a = ["a", "b", "c"]
# n = [1, 2, 3]
x = [a, n]
# print(type(x))
# print(x[1][2])

s = ["a", "b", "c", "d", "e", "f", "g"]
print(s[0])
s[0] = "x"
print(s)
s[2:5] = ["X", "Y", "Z"]
print(s)

s[2:5] = []
print(s)
s[:] = []
print(s)

n.append(11)
print(n)
n.insert(0, 200)
print(n)
print(n.pop())
print(n)
print(n.pop(0))
print(n)
del n[0]
print(n)

n.remove(6)
print(n)
# n.remove(6)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
x = [a, b]
print(x)
a += b
print(a)
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
print(x)