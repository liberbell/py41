x = {"a": 1}
y = x
y["a"] = 100
# print(x, y)

x = {"a": 1}
y = x.copy()
y["a"] = 100
# print(x, y)

fruits = {
    "apple": 100,
    "banana": 200,
    "orange": 300,
    }
print(fruits["apple"])

l = [
    ["apple", 100],
    ["banana", 200],
    ["orange", 300],
]