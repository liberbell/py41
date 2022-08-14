def counter(num=10):
    for _ in range(num):
        yield "run"

l = ["good morning", "good afternoon", "good night"]

for i in l:
    print(i)

print("#########")

def greeting():
    yield "good morning"
    yield "good afternoon"
    yield "good night"

# for g in greeting():
#     print(g)

g = greeting()
c = counter()
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print("!!!!!!")
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print("!!!!!!")
print(next(g))
# print(next(g))
