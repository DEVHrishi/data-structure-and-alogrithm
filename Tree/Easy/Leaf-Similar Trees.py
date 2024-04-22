'''Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 '''

class Solution:
    def dfs(self, node, stack):
        if not node:
            return 
        if not node.left and not node.right:
            stack.append(node.val)
        self.dfs(node.left, stack)
        self.dfs(node.right, stack)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        s1 = []
        s2 = []
        self.dfs(root1, s1)
        self.dfs(root2, s2)
        return s1 == s2
    
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(root):
            stack = [root]
            leaves = []
            
            while stack:
                node = stack.pop()
                
                if not node.left and not node.right:
                    leaves.append(node.val)
                
                if node.right:
                    stack.append(node.right)
                
                if node.left:
                    stack.append(node.left)
            
            return leaves
        
        leaves1 = get_leaves(root1)
        leaves2 = get_leaves(root2)
        
        return leaves1 == leaves2