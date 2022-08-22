class Person(object):
    kind = "human"

    def __init__(self) -> None:
        self.x = 100

    def what_is_your_kind(self):
        return self.kind


a = Person()
print(a.what_is_your_kind())
b = Person
print(b.what_is_your_kind())