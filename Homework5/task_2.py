with open('text_task_2.txt', 'r', encoding='UTF-8') as file:
    count_str = 0
    for el in file:
        count_str += 1
        stroka = el.split()
        count_words = 0
        print(f'Количество слов в строке № {count_str}: {len(stroka)}')
    print(f'Всего строк в файле: {count_str}')
