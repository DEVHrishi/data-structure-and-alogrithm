'''Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

 

Example 1:



Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
Example 2:



Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]
Example 3:



Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.'''

# tc = o(n) and sc = o(h)
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        if (not root.left and not root.right) and root.val == target:
            return None
        return root
    
# tc = o(n) and sc = o(n)
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:        
        stack = []
        node = root
        prev_node = None

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack[-1]

            if node.right and node.right is not prev_node:
                node = node.right
                continue

            stack.pop()
            
            if not node.right and not node.left and node.val == target:
                if not stack:
                    return None
        
                parent = stack[-1]
                if parent.left is node:
                    parent.left = None
                else: # parent.right is node:
                    parent.right = None

            prev_node = node
            node = None

        return root