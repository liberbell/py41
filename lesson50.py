import os

print(os.path.exists("test.txt"))
print(os.path.isfile("test.txt"))
print(os.path.isdir("design"))
os.rename("rename.txt", "test.txt")