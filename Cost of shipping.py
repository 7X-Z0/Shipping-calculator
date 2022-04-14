# Cost of shipping made by Lorenzo Guzman (7X-Z0 Github)
print('Welcome to the shipping calculator')
print('Made by: Lorenzo Guzman')

print('-------------------------------')

while True:
    weight = float(input('Please input package weight: '))
    if weight < 0:
        print('invalid input')
    elif weight > 20:
        print('Package cannot be shipped')
    else:
        break

if 0 < weight <= 1:
    print('The shipping cost is $3.5')
elif 1 < weight <= 3:
    print('The shipping cost is $5.5')
elif 3 < weight <= 10:
    print('The shipping cost is $8.5')
elif 10 < weight <= 20:
    print('The shipping cost is $10.5')


