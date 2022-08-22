class Person(object):
    
    def __init__(self, name):
        self.kind = "human"
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)