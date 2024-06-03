'''
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

 

Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
 
'''

class Solution:
    def dfs(self, node, parent, res, to_delete):
        if not node:
            return
        node.left = self.dfs(node.left,node, res, to_delete)
        node.right = self.dfs(node.right, node, res, to_delete)
        if node.val in to_delete:
            if node.left:
                res.append(node.left)
                
            if node.right:
                res.append(node.right)
            return None
        return node
                
        
        
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        res=[]

        # Handle the root node deletion
        if root.val not in to_delete:
            res.append(root)
        
        self.dfs(root, None, res, to_delete)
        
        return res