# f = open("test.txt", "w")
# f.write("TEXT insert\n")
# print("I am print", file=f)
# print("My", "name", "is", "Bob", sep="#", end="!", file=f)
# f.close()

s = """\
    AAA
    BBB
    CCC
    DDD
    """

# with open("test.txt", "w") as f:
#     f.write(s)
    # print("I am print", file=f)

with open("test.txt", "r") as f:
    print(f.read())