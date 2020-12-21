from functools import reduce
def my_func(prev_el, el):
    return prev_el * el
original_list = [el for el in range(100, 1001) if el % 2 == 0]

print(original_list)
print(reduce(my_func, original_list))