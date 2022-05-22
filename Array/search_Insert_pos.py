# Function to find insert position of K
def find_index(arr, n, K):

    # Traverse the array
    for i in range(n):

        # If K is found
        if arr[i] == K:
            return i

        # If arr[i] exceeds K
        elif arr[i] > K:
            return i

    # If all array elements are smaller
    return n


# Driver Code
arr = [1, 3, 5, 6]
n = len(arr)
K = 2
print(find_index(arr, n, K))
