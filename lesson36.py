l = [1, 2, 3]
i = 1
# del l

try:
    # () + 1
    print(l[i])
except IndexError as exc:
    print("don`t worry. {}".format(exc))
except NameError as exc:
    print("name error. {}".format(exc))
except Exception as exc:
    print("Exception error.{}".format(exc))
else:
    print("done")
finally:
    print("clean up.")