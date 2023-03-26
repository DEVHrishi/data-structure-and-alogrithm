'''
     A     
    ABA    
   ABCBA   
  ABCDCBA  
 ABCDEDCBA 
ABCDEFEDCBA
'''

ascii = 65
n = 6

for i in range(n):
    for j in range(n-i-1):
        print(' ', end = ' ')
    for j in range(i+1):
        print(chr(ascii), end = ' ')
        ascii += 1
    for j in range(i):
        print(chr(ascii - 2), end = ' ')
        ascii -= 1
    ascii = 65
    print()

