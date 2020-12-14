template = {'название': '', 'цена': '', 'количество': '', 'ед.': ''}
products = []
for i in range(int(input('Введите количество товаров, которые хотите добавить: '))):
    dict = {}
    i += 1
    for el in template.keys():
        char = input(f'Введите характеристику товара "{el}": ')
        dict.update({el: char})
    tup = (i, dict)
    products.append(tup)
print(products)
analytics = {}
for elem in products:
    for key, value in elem[1].items():
        if key in analytics:
            analytics[key].append(value)
        else:
            analytics[key] = [value]
print(analytics)