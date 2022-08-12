def menu(entree="beef", drink="wine"):
    print(entree, drink)

menu(entree="beef", drink="beer")

def menu2(food, *args, **kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        # print(k, v)
    print

menu2("banana", "apple", "lemon", entree="beef", drink="beer")