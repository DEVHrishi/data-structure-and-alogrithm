arr = [1, 2, 3, 4, 6]
n = 6

# Method 1
# tc = O(n) and sc = O(1)
for i in range(1, n+1):
    if i not in arr:
        print(i)
        break

# Method 2
# tc = O(2*n) and sc = O(n)
h = {i: 0 for i in range(1, n+1)}
for i in arr:
    h[i] = 1
for k, v in h.items():
    if v == 0:
        print(k)
        break

# Method 3
# tc = O(n) and sc = O(1)
x = 6
s = (x*(x+1)) // 2
m = sum(arr)
print(s-m)

# Method 4
# tc = O(n) and sc = O(1)
xor1 = 0
xor2 = 0
for i in range(n-1):
    xor2 = xor2 ^ arr[i]
    xor1 = xor1 ^ (i+1)
xor1 = xor1 ^ n
print(xor1 ^ xor2)