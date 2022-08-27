import tarfile

with tarfile.open("test.txt.gz", "w:gz") as tr:
    tr.add("test_dir")