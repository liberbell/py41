class Word(object):
    def __init__(self, text):
        self.text = text
    
    def __str__(self) -> str:
        return "Word!!!!!!"

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

w = Word("test")
print(len(w))
w2 = Word("######")

w + w2
print(w + w2)