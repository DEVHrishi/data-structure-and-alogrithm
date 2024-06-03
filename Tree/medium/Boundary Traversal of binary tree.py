'''Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order: 

Left boundary nodes: defined as the path from the root to the left-most node ie- the leaf node you could reach when you always travel preferring the left subtree over the right subtree. 
Leaf nodes: All the leaf nodes except for the ones that are part of left or right boundary.
Reverse right boundary nodes: defined as the path from the right-most node to the root. The right-most node is the leaf node you could reach when you always travel preferring the right subtree over the left subtree. Exclude the root from this as it was already included in the traversal of left boundary nodes.
Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary. 

Example 1:

Input:
        1 
      /   \
     2     3  
    / \   / \ 
   4   5 6   7
      / \
     8   9
   
Output: 1 2 4 8 9 6 7 3
Explanation:

Example 2:

Input:
            1
           /
          2
        /  \
       4    9
     /  \    \
    6    5    3
             /  \
            7     8

Output: 1 2 4 6 5 7 8
Explanation:

As you can see we have not taken the right subtree. 
Your Task:
This is a function problem. You don't have to take input. Just complete the function boundary() that takes the root node as input and returns an array containing the boundary values in anti-clockwise.

Expected Time Complexity: O(N). 
Expected Auxiliary Space: O(Height of the Tree).'''

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def left_traversal(self,root,ans):
        if root == None:
            return 
        if root.left == None and root.right == None:
            return
        ans.append(root.data)
        
        if root.left != None:
            self.left_traversal(root.left,ans)
        else:
            self.left_traversal(root.right,ans)
    
    def leaf_traversal(self,root,ans):
        if root == None:
            return
        if root.left == None and root.right == None:
            ans.append(root.data)
            return
        self.leaf_traversal(root.left,ans)
        self.leaf_traversal(root.right,ans)
    
    def right_traversal(self,root,ans):
        if root == None:
            return 
        if root.left == None and root.right == None:
            return 
        if root.right != None:
            self.right_traversal(root.right,ans)
        else:
            self.right_traversal(root.left,ans)
        ans.append(root.data)
            
    def printBoundaryView(self, root):
        # Code here
        ans=[]
        if root == None:
            return ans
        ans.append(root.data)
        
        self.left_traversal(root.left,ans)
        self.leaf_traversal(root.left,ans)
        self.leaf_traversal(root.right,ans)
        self.right_traversal(root.right,ans)

        return ans
    
    def printResult(result):
        for val in result:
            print(val, end=" ")
        print()
    
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.right.left = Node(5)

    solution = Solution()

    # Get the boundary traversal
    result = solution.printBoundaryView(root)

    # Print the result
    print("Boundary Traversal:", end=" ")
    solution.printResult(result)