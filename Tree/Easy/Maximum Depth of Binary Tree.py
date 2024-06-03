'''Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
'''

'''approach:
1. recursion
2. BFS
3. DFS
'''
# tc = o(n) and sc = o(n)
class Solution:
    def __init__(self):
        self.max_depth = 0
    def dfs(self, node, depth):
        if not node:
            return
        self.max_depth = max(self.max_depth, depth)
        self.dfs(node.left, depth+1)
        self.dfs(node.right, depth+1)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 1)
        return self.max_depth
    
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1+max(left_depth, right_depth)
    
class Solution:
    from collections import deque
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        result = 0
        while queue:
            level_size = len(queue)
            result += 1
            
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # check if root is None or not
        if not root:
            return 0
        # define stack
        node_stack = [(root, 1)]
        max_depth = 0

        # traverse the tree until stack is not empty
        while node_stack:
            node, depth = node_stack.pop()
            max_depth = max(max_depth, depth)
            if node.right:
                node_stack.append((node.right, depth + 1))
            if node.left:
                node_stack.append((node.left, depth + 1))

        return max_depth