class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def preOrderTraversal(root):
    if root is not None:
        print(root.key, end=" ")
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)

def inOrderTraversal(root):
    if root is not None:
        inOrderTraversal(root.left)
        print(root.key, end=" ")
        inOrderTraversal(root.right)

def postOrderTraversal(root):
    if root is not None:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.key, end=" ")

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

if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)

    print("PreOrder traversal of the given tree: ")
    preOrderTraversal(root)
    print("\nInOrder traversal of the given tree: ")
    inOrderTraversal(root)
    print("\nPostOrder traversal of the given tree: ")
    postOrderTraversal(root)