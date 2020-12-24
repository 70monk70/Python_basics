def my_func(*args):
    my_list = []
    for el in args:
        my_list.append(el)
    my_list.sort()
    return my_list[len(my_list) - 1] + my_list[len(my_list) - 2]

print(my_func(30, 10, 20))