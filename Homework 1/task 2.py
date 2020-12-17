time = int(input('Enter time in seconds: '))

if time <= 86400:
    hours = time // 3600
    minutes = (time - (hours*3600)) // 60
    seconds = (time - (hours*3600)) % 60
    print(f'The time is: {hours}:{minutes}:{seconds}')
else:
    answer = int(input('You entered a time exceeding one day. Are you sure you want to know how many hours, minutes and'
                       ' seconds are in the seconds you entered? For "yes" enter 1, for "no" - any other key: '))
    if answer == 1:
        hours = time // 3600
        minutes = (time - (hours * 3600)) // 60
        seconds = (time - (hours * 3600)) % 60
        print(f'It turns out in total: {hours}:{minutes}:{seconds}')
    else:
        print('Good bye))')