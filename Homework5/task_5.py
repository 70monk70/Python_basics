with open('text_task_5.txt', 'w') as file:
    content = input('Введите через пробел набор чисел, разделенных пробелами: ')
    file.writelines(content)
    word = content.split()
    sum = 0
    for el in word:
        try:
            el = int(el)
            sum = sum + el
        except ValueError:
            print('Ошибка типа данных')
    print(sum)