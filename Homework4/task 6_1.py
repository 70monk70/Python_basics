from sys import argv
from itertools import count
from itertools import cycle
script_name, start_number, end_number = argv
start_number = int(start_number)
end_number = int(end_number)
for el in cycle(count(start_number)):
    if el > end_number:
        break
    else:
        print(el)