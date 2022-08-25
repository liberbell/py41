from glob import glob
import os
import pathlib
import glob

print(os.path.exists("test.txt"))
print(os.path.isfile("test.txt"))
print(os.path.isdir("design"))
# os.rename("rename.txt", "test.txt")

# os.mkdir("test_dir")
# os.rmdir("test_dir")

# pathlib.Path("empty.txt").touch()
# os.remove("empty.txt")

# os.mkdir("test_dir")
# os.mkdir("test_dir/test_dir2")
# print(os.listdir("test_dir"))
# pathlib.Path("test_dir/test_dir2/empty.txt").touch()
print(glob.glob("test_dir/test_dir2/*"))