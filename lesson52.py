import tempfile

with tempfile.TemporaryFile(mode="w+") as temp:
    temp.write("hello")
    temp.seek(0)
    print(temp.read())

with tempfile.NamedTemporaryFile(delete=False):
    print(t.name)
    with open(t.name, "w+") as f:
        f.write("test\n")
        f.seek(0)
        print(f.read())