# tc = O(n) sc = O(1)
def isSorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True

# tc = O(nlogn) sc = O(n)
def isSorted(arr, n):
    return arr == sorted(arr)