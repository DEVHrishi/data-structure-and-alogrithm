# TC = O(n) and SC = O(n)
class Node (object):
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class doubly_LinkedList (object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_item(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1

    def search_item(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return print("True")
            temp = temp.next
        return print("False")


    def reverse_list(self):
        temp = self.head
        while temp:
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev
        self.head, self.tail = self.tail, self.head

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        print("No of node :", self.count)

if __name__ == '__main__':
    llist = doubly_LinkedList()
    llist.append_item(1)
    llist.append_item(2)
    llist.append_item(3)
    llist.append_item(4)
    llist.reverse_list()
    llist.print_list()