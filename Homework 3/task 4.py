# def my_func(x, y):
#     return x ** y
#
# print(my_func(2.5, -2))

def my_func(x, y):
    for i in range(abs(y)-1):
        x = (1/x) * (1/x)
    return x

print(my_func(25, -2))