# tc = O(n) and sc = O(n)
def zeros_to_end(arr, n):
    temp = [0] * n
    k = 0
    for i in range(n):
        if arr[i] != 0:
            temp[k] = arr[i]
            k += 1

    while k < n:
        temp[k] = 0
        k += 1

    for i in range(n):
        print(temp[i], end=" ")

arr = [1, 2, 0, 1, 0, 4, 0]
zeros_to_end(arr, len(arr))

# tc = O(n) and sc = O(n)
def move_zeros(arr):
    zeros = [0] * arr.count(0) # create a list of zeros with length equal to the count of zeros in the input array
    arr = [i for i in arr if i != 0] # create a new array without the zeros
    arr.extend(zeros) # append the zeros to the end of the new array
    return arr

# tc = O(n) and sc = O(1)
def zeros_to_end(arr, n):
    i = 0
    for j in range(n):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    for i in range(n):
        print(arr[i], end=" ")

arr = [1, 2, 0, 1, 0, 4, 0]
zeros_to_end(arr, len(arr))
