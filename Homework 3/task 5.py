def my_func():
    sum = 0
    while True:
        string = input('Введите числа через пробел, для выхода нажмите - q: ').split()
        for el in string:
            if el == 'q':
                print(f'Сумма равна: {sum}')
                return
            sum = sum + int(el)
        print(f'Сумма равна: {sum}')
my_func()