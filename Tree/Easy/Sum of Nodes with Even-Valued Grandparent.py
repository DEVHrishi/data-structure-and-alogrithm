'''Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.

 

Example 1:


Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
Example 2:


Input: root = [1]
Output: 0'''

# iterative approach
# tc: O(n) and sc: O(n)
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        node_stack = [(root, 1,1)]
        sum_value = 0
        while node_stack:
            node, parent, grand_parent = node_stack.pop()
            if grand_parent % 2 == 0:
                sum_value += node.val
            if node.left:
                node_stack.append((node.left, node.val, parent))
            if node.right:
                node_stack.append((node.right, node.val, parent))
        return sum_value

# recursive approach
# tc: O(n) and sc: O(n)
class Solution:
    def __init__(self):
        self.sum_value = 0
    def dfs(self, node, parent, grand_parent):
        if not node:
            return
        if grand_parent % 2 == 0:
            self.sum_value += node.val
        self.dfs(node.left, node.val, parent)
        self.dfs(node.right, node.val, parent)
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.dfs(root, 1, 1)
        return self.sum_value