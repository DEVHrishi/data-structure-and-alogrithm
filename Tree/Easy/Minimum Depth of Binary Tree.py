'''Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5'''

'''
1. stack
2. top down approach
3. bottom up approach'''

# tc = o(n) and sc = o(n)
class Solution:
    from collections import deque
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = deque([(root, 1)])
        while stack:
            node, depth = stack.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

class Solution:
    def __init__(self):
        self.min_depth = float('inf')
    def dfs(self, node, depth):
        if not node:
            return
        if not node.left and not node.right:
            self.min_depth = min(self.min_depth, depth)
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.dfs(root, 1)
        return self.min_depth
    
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.right:
            return 1+ self.minDepth(root.left)
        if not root.left:
            return 1 + self.minDepth(root.right)
        return 1+min(self.minDepth(root.left), self.minDepth(root.right))