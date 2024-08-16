# tc = O(n) and sc = O(n)
# using recursion
class Solution:
    def inorder(self, node, result):
        if not node:
            return
        self.inorder(node.left, result)
        result.append(node.val)
        self.inorder(node.right, result)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        # call recursion
        self.inorder(root, result)
        return result
        
# using stack
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # check if root is none or not
        if not root:
            return []
        # define stack
        result = []
        stack = []
        node  = root
        # traverse the tree until stack is not empty
        while stack or node:
            while node:
                stack.append(node)
                node  = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right

        return result