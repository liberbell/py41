l = [1, 2, 3]
i = 5
try:
    print(l[i])
except IndexError as exc:
    print("don`t worry. {}".format(exc))