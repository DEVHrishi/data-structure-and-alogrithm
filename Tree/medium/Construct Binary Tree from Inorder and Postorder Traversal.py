'''Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]'''

class Solution:
    def constructTree(self, postorder, l, r, dict):
        if l > r:
            return
        root_node = postorder.pop(0)
        root = TreeNode(root_node)
        index = dict[root_node]
        root.right = self.constructTree(postorder, index+1, r, dict)
        root.left = self.constructTree(postorder, l, index-1, dict)
        
        return root
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dict = {}
        for i in range(len(inorder)):
            dict[inorder[i]] = i
        postorder.reverse()
        return self.constructTree(postorder, 0, len(postorder)-1, dict)