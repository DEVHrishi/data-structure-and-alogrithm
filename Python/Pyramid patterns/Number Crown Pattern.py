'''
1          1
12        21
12       321
1234    4321
12345  54321
123456654321
'''
n = 6

for i in range(6):
    for j in range(i+1):
        print(j+1, end = ' ')
    for j in range(2*n-2*i-2):
        print(' ', end = ' ')
    for j in range(i+1, 0, -1):
        print(j, end = ' ')
    print()
