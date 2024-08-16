'''You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

 

Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.'''

# tc: O(n) and sc: O(n)
class Solution:
    def __init__(self):
        self.sum_value = 0
    def dfs(self, node, path):
        if not node:
            return
        path = path * 10 + node.val
        if not node.left and not node.right:
            self.sum_value += path
        self.dfs(node.left, path)
        self.dfs(node.right, path)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.dfs(root, 0)
        return self.sum_value

# tc: O(n) and sc: O(n)
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # check if root is none
        if not root:
            return 0
        # define stack
        node_stack = [(root, 0)]
        result = 0

        while node_stack:
            node, path_value = node_stack.pop()
            # calculate the path value
            path_value = path_value * 10 + node.val
            # if leaf node then add it to the result
            if not node.left and not node.right:
                result += path_value
            if node.left:
                node_stack.append((node.left, path_value))
            if node.right:
                node_stack.append((node.right, path_value))
        return result