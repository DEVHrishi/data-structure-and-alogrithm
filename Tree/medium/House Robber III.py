'''The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

Example 1:


Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:


Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.'''

class Solution:
    def dfs(self, root):
        if not root:
            return [0,0]
        leftpair = self.dfs(root.left)
        rightpair = self.dfs(root.right)
        with_node, without_node = root.val+leftpair[1]+rightpair[1], max(leftpair)+ max(rightpair)
        return [with_node, without_node]
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))