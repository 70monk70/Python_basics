my_list = [7, 5, 3, 3, 2]
for el in range(int(input('Enter number of new elements: '))):
    element = int(input('Enter new element of the rating: '))
    if element in my_list:
        n = my_list.count(element)
        ind = my_list.index(element)
        my_list.insert((n + ind), element)
    elif element > my_list[0]:
        ind = my_list.index(my_list[0])
        my_list.insert(ind, element)
    elif element < my_list[len(my_list)-1]:
        min_ind = len(my_list) - 1
        my_list.insert(min_ind + 1, element)
    elif element not in my_list:
        i = 0
        for ele in my_list:
            max_dig = my_list[i]
            i += 1
            if (element < max_dig) and (element > my_list[i]):
                n = my_list.count(ele)
                ind = my_list.index(ele)
                my_list.insert(ind + n, element)
                break
print(f'Current rating: {my_list}')

# my_list = [7, 5, 3, 3, 2]
# for el in range(int(input('Enter number of new elements: '))):
#     element = int(input('Enter new element of the list: '))
#     my_list.append(element)
#     my_list.sort()
#     my_list.reverse()
# print(f'Current rating: {my_list}')