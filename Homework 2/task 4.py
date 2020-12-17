answer = input('Enter a string of several words: ')
answer = answer.split(' ')
i = 0
for ind, el in enumerate(answer, 1):
    print(ind, el[:10:])
    # print(ind, el) if len(answer[ind]) <= 10 else print(ind, el[:10:])