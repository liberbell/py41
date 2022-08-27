import tarfile

# with tarfile.open("test.txt.gz", "w:gz") as tr:
#     tr.add("test_dir")

with tarfile.open("test.txt.gz", "r:gz") as tr:
    # tr.extractall(path="test_tar")
    with tr.extractfile("test_dir/sub_dir/sub.txt") as f:
        print(f.read())