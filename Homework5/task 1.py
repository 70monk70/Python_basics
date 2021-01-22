with open('text_task_1.txt', 'w') as file:
    line = input('Введите текст: ')
    while line:
        content = file.writelines(line+'\n')
        line = input('Введите текст: ')
        if not line:
            break