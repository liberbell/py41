from inspect import ismemberdescriptor


is_empty = None
print(is_empty, type(is_empty))

if is_empty is None:
    print("None!!")

print(1 == True)
print(1 is True)
print(True is True)