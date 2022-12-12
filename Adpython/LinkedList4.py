class Node:
    def __init__(self,data):
        self.data = data
        self.nextVal = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.nextVal

if __name__ == '__main__':
    ll = LinkedList()
    ll.head = Node('January')
    m2 = Node('February')
    m3 = Node('March')

    ll.head.nextVal = m2
    m2.nextVal = m3
    ll.print()

