'''Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.'''

# tc = o(n) and sc = o(n)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root,float('-inf'))]
        count = 0
        while stack:
            node, maxNum = stack.pop()
            if node.val>=maxNum:
                count+=1
            maxNum = max(maxNum,node.val)
            if node.left:
                stack.append((node.left,maxNum))
            if node.right:
                stack.append((node.right,maxNum))
        return count
    
# tc = o(n) and sc = o(h)
class Solution:
    def __init__(self):
        self.count = 0
    def traverse(self, root, max_value):
        if not root:
            return 
        if root.val >= max_value:
            self.count += 1
            max_value = root.val
        self.traverse(root.left, max_value)
        self.traverse(root.right, max_value)

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.traverse(root, float('-inf'))
        return self.count