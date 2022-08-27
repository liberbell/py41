import tempfile

with tempfile.TemporaryFile(mode="w+") as temp:
    temp.write("hello")
    temp.seek(0)
    print(temp.read())