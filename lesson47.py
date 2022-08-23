# f = open("test.txt", "w")
# f.write("TEXT insert\n")
# print("I am print", file=f)
# print("My", "name", "is", "Bob", sep="#", end="!", file=f)
# f.close()

with open("test.txt", "w") as f:
    f.write("Text insert\n")
    print("I am print", file=f)