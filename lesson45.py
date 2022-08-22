class Person(object):
    kind = "human"

    def __init__(self) -> None:
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about():
        print("about human")


a = Person()
print(a.what_is_your_kind())
b = Person
print(b.what_is_your_kind())

print(Person.kind)
print(Person.what_is_your_kind())

# print(Person.about())
Person.about()