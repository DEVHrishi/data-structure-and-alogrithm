'''Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []'''

# tc: O(n) and sc: o(n) and o(n^2) if include path storage
class Solution:
    def __init__(self):
        self.result = []
    def dfs(self, node, targetSum, temp):
        if not node:
            return
        temp.append(node.val)
        if node.val == targetSum and not node.left and not node.right:
            self.result.append(list(temp))
        self.dfs(node.left, targetSum - node.val, temp)
        self.dfs(node.right, targetSum - node.val, temp)
        temp.pop()
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        self.dfs(root, targetSum, [])
        return self.result


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, targetSum, [root.val])]
        result = []
        while stack:
            node, targetSum, temp = stack.pop()
            if node.val == targetSum and not node.left and not node.right:
                result.append(list(temp))
            if node.right:
                stack.append((node.right, targetSum - node.val, temp+[node.right.val]))
            if node.left:
                stack.append((node.left, targetSum - node.val, temp+[node.left.val]))
            
        return result