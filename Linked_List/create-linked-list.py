class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def appendItems(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def iterateItems(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next
    
    def printItems(self):
        for i in self.iterateItems():
            print(i.data, end=' -> ')
        print(None)

    def deleteItem(self, data):
        if self.head is None:
            print("Empty List")
            return
        temp = self.head
        if temp.data == data:
            print("Item Deleted from head")
            self.head = temp.next
            return
        while temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                print("Item deleted")
                return
            temp = temp.next
        print("Item not found")

    def deleteLastItem(self):
        if self.head is None:
            print("Empty List")
            return
        temp = self.head
        if temp.next is None:
            print("Item Deleted from head")
            self.head = None
            return
        while temp.next:
            if temp.next.next is None:
                temp.next = None
                print("last node deleted")
                return
            temp = temp.next
        
    def lengthOfList(self):
        c = 0
        temp = self.head
        while temp:
            c += 1
            temp = temp.next
        print(c)
        return 
    
    def searchItem(self, val):
        if self.head is None:
            print("empty list")
            return
        temp = self.head
        while temp:
            if temp.data == val:
                print("Item present")
                return
            temp = temp.next

        print("Item Not Found")
        return
    
    def createCycle(self, index):
        next_node = self.head
        pointer = self.head
        count = 0
        while next_node.next:
            if count != index:
                pointer = pointer.next
                count += 1
            next_node = next_node.next
        next_node.next = pointer


if __name__ == '__main__':
    l = linkedList()
    l.appendItems(1)
    l.appendItems(2)
    l.appendItems(3)
    l.appendItems(4)

    l.printItems()

    l.createCycle(2)
    