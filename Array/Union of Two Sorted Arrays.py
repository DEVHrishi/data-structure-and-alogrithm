arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,5]

# Method 1: Using set function
# Time Complexity: O(n) and Space Complexity: O(n)
print(set(arr1+arr2))

# Method 2: Using 2 pointer
# Time Complexity: O(n) and Space Complexity: O(n)
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5]

i = 0
j = 0

unique = []

while i < len(arr1) and j < len(arr2):
    if arr1[i] == arr2[j]:
        unique.append(arr1[i])
        i += 1
        j += 1
    elif arr1[i] < arr2[j]:
        unique.append(arr1[i])
        i += 1
    else:
        unique.append(arr2[j])
        j += 1

while i < len(arr1):
    unique.append(arr1[i])
    i += 1

while j < len(arr2):
    unique.append(arr2[j])
    j += 1

result = set(unique)

print(result)

