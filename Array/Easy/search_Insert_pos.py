# Linear search tc=O(n) sc=O(1)
def find_index(arr, K):
    for i in range(len(arr)):
        if arr[i] >= K:
            return i
    return len(arr)

arr = [1, 3, 5, 6]
K = 2
print(find_index(arr, K))

# bisect search tc=O(log(n)) sc=O(1)
import bisect
def searchInsert(nums, target):
    return bisect.bisect_left(nums, target)

# binary search tc=O(log(n)) sc=O(1)
def searchInsert(nums, target):
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low