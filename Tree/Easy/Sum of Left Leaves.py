'''Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0'''

'''
1. top down approach
2. bottom up approach
3. stack'''

class Solution:
    def __init__(self):
        self.sum_value = 0
    def dfs(self, node, left_flag):
        if not node:
            return
        if left_flag and not node.left and not node.right:
            self.sum_value += node.val
        self.dfs(node.left, True)
        self.dfs(node.right, False)
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, False)
        return self.sum_value
    
# tc = o(n) and sc = o(n)
class Solution:
    def preorder(self, node, is_left = False):
        if not node:
            return 0
        if not node.left and not node.right and is_left:
            return node.val
        return self.preorder(node.left, True) + self.preorder(node.right)
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.preorder(root, False)
    

    
# tc = o(n) and sc = o(n)
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, False)]
        result = 0
        while stack:
            node, left_flag = stack.pop()
            if left_flag and not node.left and not node.right:
                result += node.val
            if node.left:
                stack.append((node.left, True))
            if node.right:
                stack.append((node.right, False))
        return result