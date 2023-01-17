def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print('select operation: ')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

while True:
    choice = input('choose number (1/2/3/4): ')

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print('Num1 + Num2 = ', add(num1, num2))

        if choice == '2':
            print('Num1 - Num2 = ', sub(num1, num2))

        if choice == '3':
            print('Num1 * Num2 = ', mul(num1, num2))

        if choice == '4':
            print('Num1 / Num2 = ', div(num1, num2))

        next_calculation = input('Lets do next calculation (yes/no): ')
        if next_calculation == 'no':
            break

    else:
        print('Invalid Input')
