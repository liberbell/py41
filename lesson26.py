num: int = 10

def add_num(a: int, b:int) -> int:
    return a + b

r = add_num("a", "b")
# print(r)

def menu(entree="beef", drink="beer", dessert="ice"):
    print("entree: ", entree, "drink: ", drink, "deseert: ", dessert)

menu(entree="pork", drink="beer", dessert="fruit")
menu()

def test_func(x, l = []):
    l.append(x)