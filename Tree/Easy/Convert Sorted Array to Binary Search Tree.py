'''Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.'''

# tc: o(n) and sc: o(n)
class Solution(object):
    def sortedArrayToBST(self, nums):
        # Base condition...
        if len(nums) == 0:
            return None
        # set the middle node...
        mid = len(nums)//2
        # Initialise root node with value same as nums[mid]
        root = TreeNode(nums[mid])
        # Assign left subtrees as the same function called on left subranges...
        root.left = self.sortedArrayToBST(nums[:mid])
        # Assign right subtrees as the same function called on right subranges...
        root.right = self.sortedArrayToBST(nums[mid+1:])
        # Return the root node...
        return root

# tc: o(n) and sc: o(log(n))
class Solution:
    def dfs(self,l, r, nums):
        if l > r:
            return None
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = self.dfs(l, mid-1, nums)
        root.right = self.dfs(mid + 1, r, nums)
        return root
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l = 0
        r = len(nums) - 1
        return self.dfs(l, r, nums)