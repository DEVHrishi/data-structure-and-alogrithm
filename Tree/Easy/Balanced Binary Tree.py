'''Given a binary tree, determine if it is 
height-balanced
.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false'''

class Solution:
    def height_of_tree(self, node):
        if not node:
            return 0
        left_height = self.height_of_tree(node.left)
        right_height = self.height_of_tree(node.right)
        return 1 + max(left_height, right_height)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # if root is none or not
        if not root:
            return True
        # calculate the height of left and right sub tree
        left_height = self.height_of_tree(root.left)
        right_height = self.height_of_tree(root.right)

        if abs(left_height - right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False