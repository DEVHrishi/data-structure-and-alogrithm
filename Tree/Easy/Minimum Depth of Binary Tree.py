'''Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5'''

# tc = o(n) and sc = o(n)
class Solution:
    from collections import deque
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = deque([(root, 1)])
        while stack:
            node, depth = stack.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Corner Case.
        # Should never be hit unless the code is 
        # called on root = NULL
        if root == None:
            return 0
        # Base Case : 
        # Leaf node.This accounts for height = 1
        if root.left == None and root.right == None:
            return 1
        # If left subtree is Null, recur for right subtree
        if root.left == None and root.right != None:
            return self.minDepth(root.right) + 1
        # If right subtree is Null , recur for left subtree
        if root.left != None and root.right == None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1