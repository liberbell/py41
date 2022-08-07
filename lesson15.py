x = {"a": 1}
y = x
y["a"] = 100
print(x, y)

x = {"a": 1}
y = x.copy()
y["a"] = 100
print(x, y)