def g():
    for i in range(10):
        yield i

g = g()
print(type(g))
g = tuple(i for i in range(10))
print(type(g))
print(g)