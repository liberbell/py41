num: int = 10

def add_num(a: int, b:int) -> int:
    return a + b

r = add_num("a", "b")
# print(r)

def menu(entree, drink, dessert):
    print("entree: ", entree, "drink: ", drink, "deseert: ", dessert)

menu(entree="beef", drink="beer", dessert="ice")