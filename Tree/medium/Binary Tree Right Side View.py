'''Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []'''

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue= deque([root])
        result = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i + 1 == level_size:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
def rightSideView(self, root: TreeNode) -> list[int]:
        ans =[]
        
        def dfs(node =root,level=1):
            if not node: return
            
            if len(ans) < level: 
                ans.append(node.val)
            dfs(node.right,level+1)         #  <--- right first
            dfs(node.left ,level+1)         #  <--- then left

            return 

        dfs()
        return ans