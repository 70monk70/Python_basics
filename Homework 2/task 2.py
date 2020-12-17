my_list = []
i = 0
for el in range(int(input('Enter the number of items in list: '))):
    my_list.append(input('Enter next element of the list: '))
for el in range(int(len(my_list)/2)):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2
print(my_list)