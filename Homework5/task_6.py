with open('text_task_6.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()
school_objects = []
my_dict = {}
for element in content:
    school_objects.append(element.replace('\n', '').split(':'))
for el in school_objects:
    obj = el[1].split()
    count = 0
    for e in obj:
        e = e.split('(')
        for i in e:
            try:
                i = int(i)
                count += i
            except ValueError:
                pass
    my_dict.update({el[0]: count})
print(my_dict)