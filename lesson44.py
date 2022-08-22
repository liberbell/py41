class Person(object):

    kind = "human"
    
    def __init__(self, name):
        # self.kind = "human"
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

a = Person("A")
a.who_are_you()
b = Person("B")
b.who_are_you()

class T(object):

    words = []
    
    def add_word(self, word):
        self.words.append(word)

c = T()
c.add.word("add 1")
print(c.words)