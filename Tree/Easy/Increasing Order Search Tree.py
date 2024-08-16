'''Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

Example 1:

Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]'''

class Solution:
    def __init__(self):
        self.dummyNode = TreeNode(-1)
        self.res = self.dummyNode
    def dfs(self, node):
        if not node:
            return 
        self.dfs(node.left)
        self.res.right = TreeNode(node.val)
        self.res = self.res.right
        self.dfs(node.right)


    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        self.dfs(root)
        return self.dummyNode.right
    
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        stack = []
        node = root
        dummyNode = TreeNode(-1)
        result = dummyNode
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.right = node
            result = result.right
            node.left = None
            node = node.right
        return dummyNode.right