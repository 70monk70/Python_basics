with open('text_task_3.txt', 'r', encoding='UTF-8') as file:
    poor = []
    salary = []
    for el in file:
        line = el.replace('\n', '')
        words = line.split(' ')
        salary.append(words[1])
        if int(words[1]) < 20000:
            poor.append(words[0])
print(f'Сотрудники, которые имеют оклад менее 20 тыс.: {poor}, средняя величина дохода '
      f'всех сотрудников: {round(sum(map(int, salary)) / len(salary), 2)}')