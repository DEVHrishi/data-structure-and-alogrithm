'''
F
E F
D E F
C D E F
B C D E F
A B C D E F
'''

ascii = 65
n = 6

for i in range(n):
    for j in range(i+1):
        print(chr(ascii+n-1-i), end = ' ')
        ascii += 1
    ascii = 65
    print()