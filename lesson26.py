num: int = 10

def add_num(a: int, b:int) -> int:
    return a + b

r = add_num("a", "b")
# print(r)

def menu(entree="beef", drink="beer", dessert="ice"):
    print("entree: ", entree, "drink: ", drink, "deseert: ", dessert)

menu(entree="pork", drink="beer", dessert="fruit")
menu()

def test_func(x, l = None):
    if l is None:
        l = []
    l.append(x)
    return l

# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)

# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)

r = test_func(100)
print(r)

r = test_func(100)
print(r)