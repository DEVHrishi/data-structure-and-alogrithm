'''Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5'''

class Solution:
    def __init__(self):
        # initialize max depth
        self.max_depth = 0
    def dfs(self, node, depth):
        if not node:
            return
        # calculate max depth 
        self.max_depth = max(self.max_depth, depth)
        # traverse the children node
        for i in node.children:
            self.dfs(i, depth + 1)
    def maxDepth(self, root: 'Node') -> int:
        # check if root is null or not
        if not root:
            return 0
        self.dfs(root, 1)
        return self.max_depth
    
class Solution:
    from collections import deque
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        max_depth = 0
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node, depth = queue.popleft()
                max_depth = max(max_depth, depth)
                for j in node.children:
                    queue.append((j, depth+1))
        return max_depth