# tc = O(n) and sc = O(n)
# using recursion
class Solution:
    def postorder(self, node, result):
        if not node:
            return
        self.postorder(node.left, result)
        self.postorder(node.right, result)
        result.append(node.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # define empty stack
        result = []
        # call recursion
        self.postorder(root, result)
        return result

# using stack
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # check root is None or not
        if not root:
            return []
        # define  stack
        stack = [root]
        result = []
        # traverse the tree until stack is not empty
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]