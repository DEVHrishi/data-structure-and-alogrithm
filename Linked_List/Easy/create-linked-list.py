class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append_item(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def iterate_item(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def print_list(self):
        for node in self.iterate_item():
            print(node.data)
    
    def get_list(self):
        list = []
        for node in self.iterate_item():
            list.append(node.data)
        return list

    def get_length(self):
        length = 0
        for node in self.iterate_item():
            length += 1
        return length

if __name__ == '__main__':
    llist = LinkedList()
    llist.append_item(1)
    llist.append_item(2)
    llist.append_item(3)
    llist.append_item(4)
    llist.print_list()
    print(llist.get_list())
    print(llist.get_length())
