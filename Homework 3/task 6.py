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