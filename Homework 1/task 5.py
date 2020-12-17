proceeds = int(input("Enter your company's proceeds: "))
costs = int(input("Enter your company's costs: "))
if proceeds > costs:
    print(f"Your company has a profit. The company's efficency is {proceeds / costs:.2f}")
    employees = abs(int(input('Enter the number of workers: ')))
    print(f'Profit per employee {proceeds/ employees:.2f}')
elif proceeds < costs:
    print('The company is operating at a loss')
else:
    print('Proceeds and costs are equal')