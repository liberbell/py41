# d = {"x": 100, "y": 200}

# for k, v in d.items():
#     print(k, ";", v)

def say_something():
    # print("hi")
    s = "hello"
    return s

# say_something()
# print(type(say_something))

# f = say_something()
# print(f)

def what_is_this(color):
    if color == "red":
        return "tomato"
    elif color == "green":
        return "green pepper"
    else:
        return "I don`t know."
    # print(color)

result = what_is_this("red")
print(result)