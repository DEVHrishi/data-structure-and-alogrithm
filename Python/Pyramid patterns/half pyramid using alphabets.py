ascii = 65

n = int(input('Enter a number: '))
for i in range(n):
    for j in range(i+1):
        alphabet = chr(ascii)
        print(alphabet , end = ' ')
    ascii += 1
    print('\n')


'''
A
B B
C C C
D D D D
E E E E E
'''
