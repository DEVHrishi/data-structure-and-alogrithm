# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        result = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val >= low and node.val <= high:
                result += node.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
            

class Solution:
    def __init__(self):
        self.sum_value = 0
    def dfs(self, node, low, high):
        if not node:
            return
        if node.val >= low and node.val <= high:
            self.sum_value += node.val
        self.dfs(node.left, low, high)
        self.dfs(node.right, low, high)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        self.dfs(root, low, high)
        return self.sum_value