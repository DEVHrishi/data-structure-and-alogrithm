n = int(input('Enter a number: '))

if n%4 == 0:
    if n%100 == 0:
        if n%400 == 0:
            print('Number is leap year')
        else:
            print('Number is not leap year')
    else:
        print('Number is leap year')
else:
    print('Number is leap year')

