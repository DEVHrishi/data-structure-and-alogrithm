'''Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1'''

# tc = o(n) and sc = o(1)
class Solution:
    def __init__(self):
        self.diameter = 0
    def height_of_tree(self, node):
        if not node:
            return 0
        left_height = self.height_of_tree(node.left)
        right_height = self.height_of_tree(node.right)
        self.diameter = max(self.diameter, left_height+right_height)
        return 1 + max(left_height, right_height )
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.height_of_tree(root)
        return self.diameter
    
