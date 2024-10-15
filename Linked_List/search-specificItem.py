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

    def search_item(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

if __name__ == '__main__':
    llist = LinkedList()
    llist.append_item(1)
    llist.append_item(2)
    llist.append_item(3)
    llist.append_item(4)
    print(llist.search_item(3))