'''Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]'''


class Solution:
    def constructTree(self, preorder, l, r, dict):
        if l > r:
            return
        root = TreeNode(preorder.pop(0))
        index = dict[root.val]
        root.left = self.constructTree(preorder, l, index-1, dict)
        root.right = self.constructTree(preorder, index+1, r, dict)
        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dict = {}
        for i in range(len(inorder)):
            dict[inorder[i]] = i
        return self.constructTree(preorder, 0, len(preorder)-1, dict)
    
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root=TreeNode(preorder[0])
        index=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:index+1],inorder[:index])
        root.right=self.buildTree(preorder[index+1:],inorder[index+1:])
        return root