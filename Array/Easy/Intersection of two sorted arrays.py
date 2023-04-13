arr1 = [1,2,3,3,4,5]
arr2 = [2,3,3,4,4,5]

# tc = O(n^2) and sc = O(n)
l = []
v = [0]*len(arr1)
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j] and v[j] == 0:
            l.append(arr1[i])
            v[j] = 1
            break
        elif arr1[i] < arr2[j]:
            break
print(l)
        
# tc = O(n) and sc = O(k), k is the number of common elements
i = 0
j = 0
l = []
while i < len(arr1) and j < len(arr2):
    if arr1[i] == arr2[j]:
        l.append(arr1[i])
        i += 1
        j += 1
    elif arr1[i] < arr2[j]:
        i += 1
    else:
        j += 1
print(l)
