class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None;

    def append_item(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def replace_item(self, index, data):
        current_node = self.head
        count = 0
        while current_node:
            if count == index:
                current_node.data = data
                return
            current_node = current_node.next
            count += 1

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.append_item(1)
    llist.append_item(2)
    llist.append_item(3)
    llist.append_item(4)
    llist.replace_item(2, 5)
    llist.print_list()