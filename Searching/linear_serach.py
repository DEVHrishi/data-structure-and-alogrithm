# TC = O(n) and SC = O(1)

def linearSearch(arr, x, n):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
x = 5
result = linearSearch(arr, x, n)
if(result == -1):
    print("Element is not present")
else:
    print ("Element is present at index :", result)