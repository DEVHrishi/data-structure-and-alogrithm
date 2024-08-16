'''Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false'''

'''
1. recursion
2. stack
'''

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check root is none or not
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
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