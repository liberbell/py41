import tarfile

# with tarfile.open("test.txt.gz", "w:gz") as tr:
#     tr.add("test_dir")

with tarfile.open("test.txt.gz", "r:gz") as tr:
    tr.extractall(path="test_tar")