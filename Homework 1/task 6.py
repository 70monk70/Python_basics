a = abs(int(input('Enter the number of kilometers on the first day: ')))
b = abs(int(input('Enter the desired number of kilometers: ')))
day = 1
while a <= b:
    a = a * 1.10
    day += 1
print(f'On {day} day athlete has at least {b} killometers')