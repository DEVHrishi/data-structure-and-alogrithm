# TC = O(1)  and SC = O(n)
class Node (object):
    def __init__(self, data=None, prev=None, next=None):
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

    def prepend_item(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("Given Node is not present in Linked List!")
        elif n.next is None:
            new_node = Node(data)
            n.next = new_node
            new_node.pref = n
        else:
            new_node = Node(data)
            n.next.pref = new_node
            new_node.next = n.next
            n.next = new_node
            new_node.pref = n

    def add_before(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("Given Node is not present in Linked List!")
        elif n.prev is None:
            new_node = Node(data)
            n.prev = new_node
            new_node.next = n
        else:
            new_node = Node(data)
            n.prev.next = new_node
            new_node.prev = n.prev
            n.prev = new_node
            new_node.next = n

    def add_at_pos(self, data, pos):
        if pos == 1:
            self.prepend_item(data)
        elif pos == self.count:
            self.append_item(data)
        else:
            n = self.head
            count = 1
            while n is not None:
                if count == pos:
                    break
                n = n.next
                count += 1
            if n is None:
                print("Given Position is not present in Linked List!")
            else:
                new_node = Node(data)
                n.prev.next = new_node
                new_node.prev = n.prev
                new_node.next = n
                n.prev = new_node
                self.count += 1

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1

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
    llist.add_end(7)
    llist.print_list()
