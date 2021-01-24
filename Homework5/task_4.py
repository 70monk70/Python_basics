translate_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', }
rus_list = []
with open('text_task_4_first.txt', 'r', encoding='UTF-8') as file:
    content = file.read().split('\n')
    for el in content:
        el = el.split(' ', 1)
        rus_list.append(f'{translate_dict[el[0]]} {el[1]}\n')

with open('text_task_4_second.txt', 'w', encoding='UTF-8') as file:
    file.writelines(rus_list)