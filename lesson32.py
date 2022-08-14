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
print(next(g))
print("!!!!!!")
print(next(g))
print("!!!!!!")
print(next(g))
# print(next(g))
