l = [1, 2, 3]
i = 5
del l

try:
    print(l[i])
except IndexError as exc:
    print("don`t worry. {}".format(exc))
except NameError as exc:
    print("name error. {}".format(exc))