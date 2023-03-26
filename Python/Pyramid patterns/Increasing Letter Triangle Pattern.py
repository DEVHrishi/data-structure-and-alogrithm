'''
A
A B
A B C
A B C D
A B C D E
A B C D E F
'''
ascii = 65
n = 6

for i in range(6):
    for j in range(i+1):
        alphabet = chr(ascii)
        print(alphabet, end = ' ')
        ascii += 1
    ascii = 65
    print()
