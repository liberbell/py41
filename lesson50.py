import os

print(os.path.exists("test.txt"))
print(os.path.isfile("test.txt"))
print(os.path.isdir("design"))
# os.rename("rename.txt", "test.txt")

os.mkdir("test_dir")
os.rmdir("test_dir")