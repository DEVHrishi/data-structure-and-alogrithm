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

    def deleteFirstItem(self):
        if self.head is None:
            return
        self.head = self.head.next

    def deleteItem(self, data):
        current_node = self.head
        if current_node.data == data:
            self.head = current_node.next
            return
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def deleteEndItem(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

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
    llist.deleteEndItem()
    llist.print_list()
     
    


