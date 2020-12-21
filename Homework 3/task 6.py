def upper_case(text):
    new_text = []

    def int_func(word):
        res = word.title()
        return res

    words = text.split()
    for el in words:
        new_text.append(int_func(el))
    return print(f"Результат работы функции: {' '.join(new_text)}")


upper_case(input('Введите строку: '))

# def capitalize_func(text):
#     def int_func(word:str):
#         return f'{word[0].upper()}{word[1:]}'
#     words = text.split()
#     return ' '.join(list(map(lambda word: int_func(word), words)))
#
# print(capitalize_func('текстовЫЙ тЕКСТ для Проверки работы программы'))