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

def add_num(a, b):
    return a + b

print("start")
r = add_num(10, 20)
print(r)