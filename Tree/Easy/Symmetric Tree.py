'''Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false'''

class Solution:
    def sameTree(self, node1, node2):
        if (not node1 or not node2):
            return node1 == node2
        return (node1.val == node2.val) and self.sameTree(node1.left, node2.right) and self.sameTree(node1.right, node2.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.sameTree(root.left, root.right)