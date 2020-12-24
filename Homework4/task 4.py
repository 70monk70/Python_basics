from random import randrange
# def generator(*args):
#     for el in args[0]:
#         if args[0].count(el) == 1:
#             yield el
# original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
original_list = [randrange(0, 5) for el in range(int(input('Введите количество элементов: ')))]
new_list = [el for el in original_list if original_list.count(el) == 1]

print(f'Исходный список: {original_list}')
print(f'Список элементов, не имеющих повторений в исходном списке: {new_list}')

# for el in generator(original_list):
#     print(el)


