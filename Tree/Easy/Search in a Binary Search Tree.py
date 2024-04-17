'''You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []'''

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node.val == val:
                return node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return 
    
class Solution:
    def search (self, node, val):
        if not node:
            return 
        if node.val == val:
            return node
        return self.search(node.left, val) or self.search(node.right, val)
        
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.search(root, val)