f = open("test.txt", "w")
f.write("TEXT insert")
print("I am print", file=f)
f.close()