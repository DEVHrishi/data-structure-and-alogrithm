'''Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.

 

Example 1:

Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
Example 2:

Input: nums = [1,1,1]
Output: 0'''

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - (len(nums) * min(nums))
    
'''Let,
k = number of elements in nums
s = sum of elements in nums
m = minumum number of moves
e = element at all indices in final array (Eg., [a, b, d, a, c] will turn to [e, e, e, e, e])

Sum of all elements in the final array is going to be k * e.

On each move, the sum of the original array is going to increase by k - 1. So after m moves, the sum will increase by m(k - 1).

Hence, we have,
s + m(k - 1) = k * e ---- equation (i)

In this equation, e is the only unknown other than m. How can we find e? Whatever the smallest integer is in nums, plus the number of moves m, will be equal to e. This is because with each m, we only increment the value by 1. So,

min + m = e ---- equation (ii)

Combining (i) and (ii),

s + m(k - 1) = k(min + m)

Simplify for m,

m = s - (k * min)

Hence, we return the sum(nums), minus the product of the number of elements in nums and the smallest element in nums.'''