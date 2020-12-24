def fact(*args):
    i = 0
    res = 1
    for el in range(args[0]):
        if i < args[0]:
            i += 1
            res = res * (el + 1)
            yield res
        else:
            break


try:
    n = int(input('Введите число, факториал которого хотите получить: '))
    for el in fact(n):
        print(el)
except ValueError:
    print(None)
