# Program 4 - Python program to demonstrate stack implementation using linked list
# node class

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    # Initializing a stack.
    def __init__(self):
        self.head = Node("head")
        self.size = 0
        

# String representation of the stack in Linked List form by appending "->"
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0

# Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

# Popping a value from stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


# main Code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 16):
        stack.push(i)
    print(f"Stack: {stack}")
    for _ in range(1, 11):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
