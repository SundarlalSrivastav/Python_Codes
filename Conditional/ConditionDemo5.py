# To check which number is greater.

num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))

if num_1 > num_2:
    print(f'Number {num_1} is greater than {num_2} number')
elif num_1 < num_2:
    print(f'Number {num_2} is greater than {num_1} number')
else:
    print(f'Number {num_1} is equal to {num_2} number')