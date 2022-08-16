# raise IndexError("test error")

class UpperCaseError(Exception):
    pass

def check():
    words = ["apple", "orange", "banana", "MELON"]
    for word in words:
        if word.isupper():
            # raise UpperCaseError(word)

try:
    check()
except UpperCaseError as exc:
    print("This is my fault. {}".format(exc))