def menu(entree="beef", drink="wine"):
    print(entree, drink)

menu(entree="beef", drink="beer")

def menu2(**kwargs):
    print(kwargs)

menu2(entree="beef", drink="beer")