from sys import argv
from itertools import cycle

script_name, number = argv
number = int(number)
my_list = [1, 2, 3]
i = 0
for el in cycle(my_list):
    i += 1
    if i > number:
        break
    else:
        print(el)