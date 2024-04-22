'''Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1'''
'''
1. inorder traversal
'''
class Solution:
    def __init__(self):
        self.min_distance = float('inf')
        self.prior_node = float('-inf')
    def traverse_tree(self, node):
        # check if node is none or not
        if not node:
            return 
        self.traverse_tree(node.left)
        self.min_distance = min(self.min_distance, node.val - self.prior_node)
        self.prior_node = node.val
        self.traverse_tree(node.right)
        
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.traverse_tree(root)
        return self.min_distance
    
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # check if root is none or not
        if not root:
            return 0
        # define stack
        stack = []
        node = root
        min_distance = float('inf')
        prior_value = float('-inf')
        # traverse the tree until stack is not empty
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            min_distance = min(min_distance, node.val - prior_value)
            prior_value = node.val
            node = node.right
        return min_distance