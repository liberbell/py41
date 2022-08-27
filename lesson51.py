# import tarfile
import zipfile

# with tarfile.open("test.txt.gz", "w:gz") as tr:
#     tr.add("test_dir")

# with tarfile.open("test.txt.gz", "r:gz") as tr:
#     # tr.extractall(path="test_tar")
#     with tr.extractfile("test_dir/sub_dir2/sub.txt") as f:
#         print(f.read())

with zipfile.ZipFile("test.zip", "w") as zip_file:
    zip_file.write("test_dir")
    zip_file.write("test_dir/test.txt")