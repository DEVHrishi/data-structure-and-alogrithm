num_rows = int(input("Enter the number of rows in the pyramid: "))

for i in range(num_rows):
    for j in range(num_rows-i-1):
        print(" ", end=" ")
    for j in range(2*i+1):
        print("*", end=" ")
    print()

'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''
