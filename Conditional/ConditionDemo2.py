#Program to calculate the value of 2 variables.

a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))

print('press 1 for Addition')
print('press 2 for Subtraction')
print('press 3 for Multiplication')
print('press 4 for Division')
print('press 5 for Modulo')

c = int(input('Enter your selection: '))

if c == 1:
    print(f'Sum is: {a + b}')
elif c == 2:
    print(f'Sub is: {a - b}')
elif c == 3:
    print(f'Multi is: {a * b}')
elif c == 4:
    if b != 0:
        print(f'Div is: {a / b}')
    else:
        print('Cannot divide by zero')
elif c == 5:
    print(f'Reminder is: {a % b}')
else:
    print('Invalid input')
