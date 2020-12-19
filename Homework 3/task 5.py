def my_func(*args):
    my_list = []
    for el in args[0]:
        my_list.append(el)
        my_list.sort()
    sum = 0
    for el in my_list:
        if el != 'q':
            sum += int(el)
        else:
            break
    return sum

x = input('Введите строку чисел, для выхода нажмите - q: ').split(' ')
print(my_func(x))