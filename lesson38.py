import sys
# import lesson_package.utils
from lesson_package import utils as u
# from lesson_package.utils import say_twice

# l = sys.argv
# print(l[1])

# for i in l:
#     print(i)

# r = lesson_package.utils.say_twice("hello")
r = u.say_twice("bye")
# r = say_twice("sleepy")
print(r)