import tempfile

with tempfile.TemporaryFile(mode="w+") as temp:
    temp.write("hello")
    temp.seek(0)
    print(temp.read())

with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, "w+") as f:
        f.write("test\n")
        f.seek(0)
        print(f.read())

with tempfile.TemporaryDirectory() as td:
    print(td)

temp_dir = tempfile.mkdtemp()
print(temp_dir)
