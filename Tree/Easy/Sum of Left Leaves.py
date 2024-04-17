'''Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0'''

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

        # check root is None or not
        if not root:
            return 0
        # define stack
        stack = [(root, False)]

        sum_of_left_nodes = 0
        # traverse the tree untill stack is not empty
        while stack:
            node, leaf = stack.pop()
            if node.left:
                stack.append((node.left, True))
                leaf = False
            if node.right:
                stack.append((node.right, False))
                leaf = False
            if leaf:
                sum_of_left_nodes += node.val
        return sum_of_left_nodes