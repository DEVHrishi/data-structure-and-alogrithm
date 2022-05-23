# first approach
array_num =  [1,5,6]
array_num.sort(reverse =True)
print(array_num[2])

# Second approach

import sys
def thirdLargest(arr, arr_size):
    if (arr_size < 3):
        print(" Invalid Input ")
        return
    first = arr[0]
    second = -sys.maxsize
    third = -sys.maxsize

    for i in range(1, arr_size):
        if (arr[i] > first):
            third = second
            second = first
            first = arr[i]

        elif (arr[i] > second):
            third = second
            second = arr[i]

        elif (arr[i] > third):
            third = arr[i]

    print("The third Largest element is",third)
arr = [12, 13, 1, 10, 34, 16]
n = len(arr)
thirdLargest(arr, n)