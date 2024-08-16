'''Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false'''

'''
1. dfs in recursion and stack
'''

class Solution:
    def is_same(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.is_same(p.left, q.left) and self.is_same(p.right, q.right)

    def dfs(self, node, subRoot):
        if not node:
            return False 
        if self.is_same(node, subRoot):
            return True
        return self.dfs(node.left, subRoot) or self.dfs(node.right, subRoot)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return self.dfs(root, subRoot) 
    

class Solution:
    from collections import deque
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # define deque
        queue = deque([(p, q)])
        # traverse the tree until queue is not empty
        while queue:
            left_tree, right_tree = queue.pop()

            # check nodes value same or not
            if not left_tree and not right_tree:
                continue
            if not left_tree or not right_tree or (left_tree.val != right_tree.val):
                return False
            
            queue.append((left_tree.left, right_tree.left))
            queue.append((left_tree.right, right_tree.right))
        return True
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        stack = deque([root])
        
        while stack:
            node = stack.pop()
            
            if node.val == subRoot.val and self.isSameTree(node, subRoot):
                return True
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return False