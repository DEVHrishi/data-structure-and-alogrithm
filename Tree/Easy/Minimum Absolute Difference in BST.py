'''Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1'''

# tc: o(n) and sc: o(h) in worst case o(n) and in best case O(log n)
class Solution:
    def __init__(self):
        self.min_diff = float('inf')
        self.prev = None
        
    def dfs(self, node):
        if not node:
            return
        # Traverse the left subtree
        self.dfs(node.left)
        
        # Compute the difference with the previous node in in-order traversal
        if self.prev is not None:
            self.min_diff = min(self.min_diff, node.val - self.prev)
        
        # Update the previous node to the current node
        self.prev = node.val
        
        # Traverse the right subtree
        self.dfs(node.right)
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.min_diff


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        cur, stack, minDiff, prev = root, [], 10**5, -10**5
        
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            minDiff = min(minDiff, node.val - prev)
            prev = node.val
            cur = node.right
        
        return minDiff