n = abs(int(input("Enter a number: ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print(f'Maximum digit in a number: {max}')
        break