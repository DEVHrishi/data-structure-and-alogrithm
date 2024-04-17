# tc = O(n) and sc = O(n)
# using recursion
class Solution:
    def preorder(self, node, result):
        if not node:
            return
        result.append(node.val)
        self.preorder(node.left, result)
        self.preorder(node.right, result)
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # define empty stack
        result = []
        # call recursion
        self.preorder(root, result)
        return result
    
# using stack
class Solution:
        def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            # check if root is None or not
            if not root:
                return []

            # define stack
            stack = [root]
            result = []
            
            # traverse the tree until stack is not empty
            while stack:
                node = stack.pop()
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return result
        