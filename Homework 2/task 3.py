month = int(input('Enter the month as an integer (from 1 to 12): '))
season = ['winter', 'spring', 'summer', 'autumn']
year = {(1, 2, 12): season[0], (3, 4, 5): season[1], (6, 7, 8): season[2], (9, 10, 11): season[3]}
if month <= 12:
    for key, value in year.items():
        if month in key:
            print(f'Season with month # {month} is {value}')
            break
else:
    print(f"There aren't month # {month}")