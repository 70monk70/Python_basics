def func(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return None
x = float(input('Введите первое число: '))
y = float(input('Введите второе число: '))
print(f'Результат деления числа {x} на число {y}: {func(x, y)}')