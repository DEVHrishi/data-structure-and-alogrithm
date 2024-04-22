'''
1. recursive
2. stack
'''
# tc = o(n^2) and sc = o(1)
def height(node):
    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)

    return max(left_height, right_height) + 1

def is_height_balanced(node):
    if node is None:
        return True

    left_height = height(node.left)
    right_height = height(node.right)

    if abs(left_height - right_height) <= 1 and is_height_balanced(node.left) and is_height_balanced(node.right):
        return True

    return False

def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
    
        stack = [(root, 1)]  # Stack stores tuples (node, height)
        
        while stack:
            node, height = stack.pop()
            
            # Check if the current node is a leaf node
            if not node.left and not node.right:
                continue
            
            # If the current node has only one child
            if not node.left or not node.right:
                if height > 2:
                    return False
            
            # If the heights of left and right subtrees differ by more than 1
            if abs(self.height_of_tree(node.left) - self.height_of_tree(node.right)) > 1:
                return False
            
            # Push child nodes onto the stack with updated heights
            if node.left:
                stack.append((node.left, height + 1))
            if node.right:
                stack.append((node.right, height + 1))
    
        return True