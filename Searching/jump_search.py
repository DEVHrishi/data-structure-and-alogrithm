# TC = O(√n) and SC = O(1)

import math

def jumpSearch(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = 8
p = jumpSearch(arr, key)
print("Index of", key, "is", p)