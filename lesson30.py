# def outer(a, b):
#     def inner():
#         return a + b

#     return inner

# f = outer(1, 2)
# r = f()
# print(r)

# def circle_area_func(pi):
#     def circle_area(radius):
#         return pi * radius * radius

#     return circle_area

# cal1 = circle_area_func(3.14)
# cal2 = circle_area_func(3.141592)

# print(cal1(10))
# print(cal2(10))

def print_more(func):
    def wrapper(*args, **kwargs):
        print("func: ", func.__name__)
        print("args: ", args)
        print("kwargs:", kwargs)
        result = func(*args, **kwargs)
        print("result:", result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper

@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

@print_info
def sub_num(a, b):
    return a - b

s = sub_num(20, 10)
print(s)
# print("start")
# r = add_num(10, 20)
# print("end")

# print(r)

# f = print_info(add_num)
# r = f(10, 20)
# print(r)