'''Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

 

Example 1:


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
Example 2:


Input: root = [1,null,2,null,0,3]
Output: 3'''

# tc: O(n) and sc: O(n)
class Solution:

    def dfs(self, root, mx, mn):
        if not root:
            return 0
        # calculate max value
        max_value = max(abs(root.val - mx), abs(root.val - mn)) 

        # calculate max and min
        mx, mn = max(root.val, mx), min(root.val, mn)

        return max(max_value, self.dfs(root.left, mx, mn), self.dfs(root.right, mx, mn))

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, root.val, root.val)

# tc: O(n) and sc: O(n)
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # define stack
        node_stack = [(root, root.val, root.val)]
        max_value = 0

        while node_stack:
            node, mx, mn = node_stack.pop()
            # calculate max difference value
            max_value = max(max_value, abs(node.val - mx), abs(node.val - mn))

            # calculate max and min
            mx, mn = max(node.val, mx), min(node.val, mn)

            if node.left:
                node_stack.append((node.left, mx, mn))
            if node.right:
                node_stack.append((node.right, mx, mn))
        return max_value