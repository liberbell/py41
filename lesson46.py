class Word(object):
    def __init__(self, text):
        self.text = text
    
    def __str__(self) -> str:
        return "Word!!!!!!"


w = Word("test")
print(w)