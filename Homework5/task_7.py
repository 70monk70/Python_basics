import json

with open('text_task_7.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()

firm = {}
profit_list = []
damage_list = []
result = []
for element in content:
    company, form, earnings, damages = element.split()
    profit = int(earnings) - int(damages)
    firm.update({company: profit})
    if profit > 0:
        profit_list.append(profit)
    else:
        damage_list.append(profit)
result.append(firm)
try:
    average_profit = dict({'average_profit': round(sum(profit_list) / len(profit_list))})
    result.append(average_profit)
    average_damage = dict({'average_damage': sum(damage_list) / len(damage_list)})
    result.append(average_damage)
except ZeroDivisionError:
    None

with open('text_task_7.json', 'w') as file:
    content = json.dumps(result, ensure_ascii=False)
    file.write(content)
