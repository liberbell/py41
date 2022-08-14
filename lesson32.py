l = ["good morning", "good afternoon", "good night"]

for i in l:
    print(i)

print("#########")

def greeting():
    yield "good morning"
    yield "good afternoon"
    yield "good night"

for g in greeting():
    print(g)