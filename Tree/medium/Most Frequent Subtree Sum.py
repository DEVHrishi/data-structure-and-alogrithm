'''Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

 

Example 1:


Input: root = [5,2,-3]
Output: [2,-3,4]
Example 2:


Input: root = [5,2,-5]
Output: [2]'''

class Solution:
    from collections import defaultdict
    def __init__(self):
        self.dict = defaultdict(int)
        self.result = []
    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        sum_value = node.val + left + right
        self.dict[sum_value] += 1
        return sum_value
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        val = max(self.dict.values())
        for k, v in self.dict.items():
            if v == val:
                self.result.append(k)
        return self.result