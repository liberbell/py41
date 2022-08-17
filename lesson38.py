# import sys
# import lesson_package.utils
# from lesson_package.tools import utils as u
# from lesson_package.utils import say_twice
# from lesson_package.talk import human
# from lesson_package.talk import animal
# from lesson_package.talk import *
try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils

# l = sys.argv
# print(l[1])

# for i in l:
#     print(i)

# r = lesson_package.utils.say_twice("hello")
# r = u.say_twice("bye")
# r = say_twice("sleepy")
# print(r)

# print(animal.sing())
# print(animal.cry())
# print(human.sing())
# print(human.cry())

print(utils.say_twice("word"))