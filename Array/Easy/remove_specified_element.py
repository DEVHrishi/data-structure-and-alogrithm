# remove first element only
from array import *
arr_input = array('i',[1, 3, 5, 3, 7, 1, 9, 3])
print("Original array:", str(arr_input))
print('Remove the first occurrence of 3 from the said array:')
arr_input.remove(3)
print("New array:", str(arr_input))

# remove all occurrences of a particular element from the said array
# tc = o(n) sc = o(1)
def removeElement(nums, val):
        x = 0
        for i in range(0,len(nums)):
            if(nums[i] != val):
                nums[x] = nums[i]
                x+=1
        return (x)

print("\nRemove all occurrences of 3 from the said array:", removeElement(arr_input, 3))