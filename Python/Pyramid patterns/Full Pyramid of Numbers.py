'''Write a Python program to print the following pattern.
        1 
      2 3 2 
    3 4 5 4 3 
  4 5 6 7 6 5 4 
5 6 7 8 9 8 7 6 5
'''

rows = 5

for i in range(1, rows+1):
    # print spaces
    print(" " * (2*rows-2*i), end="")
  
    # print increasing numbers
    for j in range(i, 2*i):
        print(j, end=" ")
    
    # print decreasing numbers
    for k in range(2*i-2, i-1, -1):
        print(k, end=" ")
    
    # print newline character
    print()






