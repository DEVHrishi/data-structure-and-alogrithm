# iterative approach TC = O(log3 n) and SC = O(1)
def ternarySearch(l, r, key, arr):
        while r >= l:
            mid1 = l + (r-l) // 3
            mid2 = r - (r-l) // 3

            if key == arr[mid1]:
                return mid1
            if key == mid2:
                return mid2

            if key < arr[mid1]:
                r = mid1 - 1
            elif key > arr[mid2]:
                l = mid2 + 1
            else:
                l = mid1 + 1
                r = mid2 - 1
        return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = 0
r = 9
key = 5
p = ternarySearch(l, r, key, arr)
print("Index of", key, "is", p)

# recursive approach TC = O(log3 n) and SC = O(log3 n)

def ternarySearch(l, r, key, arr):
        while r >= l:
            mid1 = l + (r-l) // 3
            mid2 = r - (r-l) // 3

            if key == arr[mid1]:
                return mid1
            if key == mid2:
                return mid2

            if key < arr[mid1]:
                return ternarySearch(l, mid1-1, key, arr)
            elif key > arr[mid2]:
                return ternarySearch(mid2+1, r, key, arr)
            else:
                return ternarySearch(mid1+1, mid2-1, key, arr)
        return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = 0
r = 9
key = 5
p = ternarySearch(l, r, key, arr)
print("Index of", key, "is", p)