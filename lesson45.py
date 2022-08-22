class Person(object):
    kind = "human"

    def __init__(self) -> None:
        self.x = 100


a = Person()
print(a.kind)
b = Person
print(b.kind)