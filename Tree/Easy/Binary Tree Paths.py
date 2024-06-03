'''Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]'''

# tc: O(n) and sc: o(h) in worst cast O(log n)and path storage: O(n^2)
class Solution:
    def dfs(self, node: Optional[TreeNode], path: str, result: List[str]) -> None:
        if not node:
            return
        # Check if the current node is a leaf
        if not node.left and not node.right:
            result.append(path)
            return
        # Traverse the left child
        if node.left:
            self.dfs(node.left, path + '->' + str(node.left.val), result)
        # Traverse the right child
        if node.right:
            self.dfs(node.right, path + '->' + str(node.right.val), result)
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        result = []
        self.dfs(root, str(root.val), result)
        return result

# tc: O(n) and sc: o(n)
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # check if root is none or not
        if not root:
            return []
        # define stack
        node_stack = [(root, str(root.val))]
        result = []
        # traverse the tree and find leaf node
        while node_stack:
            node, path = node_stack.pop()
            # check if leaf or not
            if not node.left and not node.right:
                result.append(path)
            if node.left:
                node_stack.append((node.left, path+'->'+str(node.left.val)))
            if node.right:
                node_stack.append((node.right, path+'->'+str(node.right.val)))
        return result