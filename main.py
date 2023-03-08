class Node():
    def __init__(self):
        self.data=None
        self.next=None
    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data
    def setNext(self, next):
        self.next = next
    def getNext(self):
        return self.next
class LinkedList():
    def __init__(self):
        self.head=None
        self.size=0
    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.size == 0:
            self.head = newNode
            self.size = self.size + 1

        else:
            newNode.setNext(self.head)
            self.head = newNode
            self.size = self.size + 1
            print(data)
    def insertAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(newNode)
        self.size = self.size + 1
        print(data)

l=LinkedList()
l.insertAtBeginning(1)
l.insertAtEnd(10)
l.insertAtEnd(4)
l.insertAtEnd(6)
print(l.size)