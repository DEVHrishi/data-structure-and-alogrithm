arr = [4,1,2,1,2]

# tc = O(n*n) and sc = O(1)
for i in range(len(arr)):
    num = arr[i]
    c = 0
    for j in range(len(arr)):
        if num == arr[j]:
            c += 1
    if c == 1:
        print(num)
        break

# tc = O(n) and sc = O(n)
from collections import Counter

d = Counter(arr)
for k, v in d.items():
    if v == 1:
        print(k)
        break

# tc = O(n) and sc = O(1)
s = set(arr)
for i in s:
    if arr.count(i) == 1:
        print(i)
        break

# tc = O(n) and sc = O(1)
xor = 0
for i in range(len(arr)):
    xor = xor ^ arr[i]
print(xor)