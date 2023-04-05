#tc = O(n) and sc = O(1)
arr = [4, 2, 5, 5, 1, 9, 4]
mx = arr[0]
for i in range(1, len(arr)):
    if arr[i] > mx:
        mx = arr[i]
print(mx)

#tc = O(nlogn) and sc = O(n)
s = sorted(arr)
print(s[-1])

#tc = O(n) and sc = O(1)
print(max(arr)) 
