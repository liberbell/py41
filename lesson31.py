l = ["Mon", "tue", "Wed", "Thu", "fri", "sat", "Sun"]

def change_words(words, func):
    for word in words:
        print(func(word))