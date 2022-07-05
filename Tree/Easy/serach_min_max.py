class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def count(Node):
    if Node is None:
        return 0
    return 1 + count(Node.left) + count(Node.right) 
    
def minValueNode(Node):
    current = Node
    while current.left is not None:
        current = current.left
    return current

def maxValueNode(Node):
    current = Node
    while current.right is not None:
        current = current.right
    return current

def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    # return the (unchanged) node pointer
    return node

def search(Node, key):
    if Node is None:
        return print("Not found")
    if Node.key == key:
        return print("Found")
    if key < Node.key:
        return search(Node.left, key)
    return search(Node.right, key)

def print_tree(Node):
    if Node is None:
        return
    print_tree(Node.left)
    print(Node.key, end=" ")
    print_tree(Node.right)


if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    print("InOrder traversal of the given tree")
    print_tree(root)
    print("\n")
    print("Number of nodes in tree: %d" % count(root))
    print("\n")
    print("Minimum value node: %d" % minValueNode(root).key)
    print("\n")
    print("Maximum value node: %d" % maxValueNode(root).key)
    print("\n")
    print("Searching for key:" )
    search(root, 100)
    


