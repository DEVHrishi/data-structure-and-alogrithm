'''Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:


Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:


Input: root = [2,2,2]
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.'''

# tc = o(n) and sc = o(n)
class Solution:
    def __init__(self):
        self.min_value = float('inf')
        self.second_min_value = float('inf')

    def dfs(self, node):
        if not node:
            return
        
        # Update min_value and second_min_value based on the current node value
        if node.val < self.min_value:
            self.second_min_value = self.min_value
            self.min_value = node.val
        elif node.val < self.second_min_value and node.val != self.min_value:
            self.second_min_value = node.val

        # Recursive DFS traversal
        self.dfs(node.left)
        self.dfs(node.right)

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        
        self.dfs(root)

        # If second_min_value is still infinity, it means there is no second minimum value
        if self.second_min_value == float('inf'):
            return -1
        
        return self.second_min_value
    

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # Initialize minimum value as root's value
        min_value = root.val

        # Initialize second minimum as positive infinity
        second_min = float('inf')

        stack = [root]

        while stack:
            node = stack.pop()

            # Update second minimum if node's value is greater than minimum value
            if min_value < node.val< second_min:
                second_min = node.val
            
            # Push left and right child nodes onto stack
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

         # Return second minimum value if it has been updated, otherwise -1
        return second_min if second_min != float('inf') else -1