# Iterative approach TC = O(log n) and SC = O(1)
def binarySearch(arr, x, low, high):

    while(low <= high):
        mid = low + (high - low)//2
        if (arr[mid] == x):
            return mid
        elif(arr[mid] < x):
            low = mid + 1   
        else:
            high = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7]
x = 5
result = binarySearch(arr, x, 0, len(arr)-1)
if(result == -1):
    print("Element is not present")
else:
    print ("Element is present at index :" , result)

# recursive approach TC = O(log n) and SC = O(log n)

def binarySearch(arr, x, low, high):

    while(low <= high):
        mid = low + (high - low)//2
        if (arr[mid] == x):
            return mid
        elif (arr[mid] < x):
            return binarySearch(arr, x, mid+1, high)
        else:
            return binarySearch(arr, x, low, mid-1)
    return -1

arr = [1, 2, 3, 4, 5, 6, 7]
x = 5
result = binarySearch(arr, x, 0, len(arr)-1)
if(result == -1):
    print("Element is not present")
else:
    print ("Element is present at index :" , result)

