"""
test##############
"""
# def g():
#     for i in range(10):
#         yield i

# g = g()
# print(type(g))
# g = (i for i in range(10) if i % 2 == 0)
# print(type(g))
# print(g)

# for x in g:
#     print(x)

from tokenize import Name
from unicodedata import name


animal = "cat"

def f():
    # print(animal)
    # global animal
    # animal = "dog"
    # print("after", locals())
    """Test func doc"""
    print(f.__name__)
    print(f.__doc__)

f()
print(__name__)
print("global", globals())
