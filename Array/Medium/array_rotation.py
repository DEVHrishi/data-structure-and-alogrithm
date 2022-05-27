def rotateArray(a,d):
    temp = []
    n=len(a)
    for i in range(d,n):
        temp.append(a[i])
    i = 0
    for i in range (0,d):
        temp.append(a[i])
    a=temp.copy()
    return a
 
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, 2))

# Time complexity = O(n)
# Space complexity = O(1)

# List slicing approach to rotate the array
def rotateArray(a,d):
    n=len(a)
    a[:]=a[d:n]+a[0:d]
    return a

arr = [1, 2, 3, 4, 5, 6]

print("Rotated list is")
print(rotateArray(arr,2)) 

# Time complexity = O(n)
# Space complexity = O(n)