class Person(object):
    kind = "human"

    def __init__(self) -> None:
        self.x = 100

    @classmethod
    def what_is_your_kind(self):
        return cls.kind


a = Person()
print(a.what_is_your_kind())
b = Person
print(b.what_is_your_kind())