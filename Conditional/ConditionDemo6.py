# Take 3 numbers as input and then check which one is greater.

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

if a > b and a > c:
    print(f'The number {a} is greater than {b} & {c}.')
elif b > a and b > c:
    print(f'The number {b} is greater than {c} & {a}.')
elif c > a and c > b:
    print(f'The number {c} is greater than {a} & {b}.')
elif a == c and c > b:
    print(f'The number {a} & {c} both are equal and greater than {b}.')
elif c == b and c > a:
    print(f'The number {b} & {c} both are equal and greater than {a}.')
elif a == b and b > c:
    print(f'The number {a} & {b} both are equal and greater than {c}.')
elif a == b == c:
    print(f'All are equal {a}  {c} {b}.')
else:
    print('None of the above.')
