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