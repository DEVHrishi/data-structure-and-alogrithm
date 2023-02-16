a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
c = int(input('Enter a number: '))

sol1 = (-b-(b**2 - 4*a*c)**0.5)/2*a
sol2 = (-b+(b**2 - 4*a*c)**0.5)/2*a

print('Solution of the quadratic equation is: {} and {}'.format(sol1,sol2))