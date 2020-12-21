from random import randrange
def generator(*args):
    i = 0
    while i < len(args[0])-1:
        i += 1
        if args[0][i] > args[0][i-1]:
            yield args[0][i]
original_list = [randrange(0, 100) for elem in range(int(input('Введите количество элементов исходного списка: ')))]
new_list = []
for el in generator(original_list):
    new_list.append(el)
print(f'Исходный список: {original_list}')
print(f'Новый список: {new_list}')
