#To check whether input number is +ve, -ve, or zero.

a = float(input('Enter a number: '))

if a > 0:
    print('Entered number is positive')
elif a == 0:
    print('Number is zero')
elif a < 0:
    print('Number is negative')
else:
    print('Enter valid number')