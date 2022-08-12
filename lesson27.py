def say_somethinsg(word):
    print(word)

say_somethinsg("Hi")

def say_somethinsg2(*args):
    print(args)
    for arg in args:
        print(arg)

say_somethinsg2("Hi", "Eric", "How", "are", "you.")