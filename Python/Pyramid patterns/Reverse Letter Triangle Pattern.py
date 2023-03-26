'''
A B C D E F
A B C D E 
A B C D
A B C
A B
A
'''
ascii = 65
n = 6

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(ascii), end = ' ')
        ascii += 1
    ascii = 65
    print()