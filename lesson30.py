def outer(a, b):
    def inner():
        return a + b

    return inner

f = outer(1, 2)
print(f)