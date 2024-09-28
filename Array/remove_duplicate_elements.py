# brute force method tc=O(n log n) sc=O(1)
def test(nums):
    return (sorted(set(nums)))

array_num = [1,1,2]
print(test(array_num))
n = len(test(array_num))
print(n)


# efficient approach tc=o(n) sc=o(1)
def removeDuplicates(nums):
    x = 1
    for i in range(len(nums)-1):
        if(nums[i] != nums[i+1]):
            nums[x] = nums[i+1]
            x += 1
    return(x)

array_num = [1,1,2]

print("\nAfter removing duplicate elements from the said array no of elements:", removeDuplicates(array_num))
