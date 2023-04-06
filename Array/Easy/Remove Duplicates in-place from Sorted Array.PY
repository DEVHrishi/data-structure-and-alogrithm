arr = [1, 1, 2, 2, 2, 3, 3]

#tc = O(n) sc = O(n)
print(set(arr))

# tc = O(n^2) sc = O(n)
l = []
for i in range(len(arr)):
    if arr[i] not in l:
        l.append(arr[i])
print(l)

# tc = O(n) sc = O(1)
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
i = 0
for j in range(1, len(arr)):
    if arr[j] != arr[i]:
        i += 1
        arr[i] = arr[j]
arr = arr[:i+1]
print(arr)
