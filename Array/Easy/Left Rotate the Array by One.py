arr = [1, 2, 3, 4, 5]

# tc = O(n) and sc = O(1)
n = len(arr)
temp = arr[0]
for i in range(n-1):
    arr[i] = arr[i+1]
arr[n-1] = temp

print(arr)

