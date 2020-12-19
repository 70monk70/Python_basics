def func(name, year, city, email, telephone):
    return (f'Привет, {name}! Вы {year} года рожддения, из города {city}.'
            f'Ваши контакты: email - {email}, телефон - {telephone}')

print(func(name=input('Как Вас зовут? '), year=input('Какого Вы года рождения? '),
           city=input('Из какого Вы города? '), email=input('Какой Ваш email? '),
           telephone=input('Какой у Вас телефон? ')))