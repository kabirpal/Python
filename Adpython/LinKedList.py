class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print('LinkedList is empty')
            return
        itr = self.head
        ll = ''
        while itr:
            ll += str(itr.data)+'---->'
            itr = itr.next
        print(ll)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)


    def insert_at(self, index , data):
        if index<0 or index>self.get_length():
            raise Exception('Invalid Index')

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self,index):
        if index<0 or index> self.get_length():
            raise Exception('Index out of range')

        if index ==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count +=1

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        for i in range(len(itr)):
            if itr == data_after:
                node = Node(data_to_insert,itr.next)
                self.head = node
                return

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()
    ll.insert_after_value(7,90)


    # llr = LinkedList()
    # llr.insert_at_begining(78)
    # llr.insert_at_begining(67)
    # llr.insert_at_begining(56)
    # llr.print()
    # print('Length:',llr.get_length())

    # llr.insert_at_end(65)
    # llr.insert_at_end(905)
    # llr.insert_at_end(615)
    # llr.print()

    # # llr.insert_at(1,"blueberry")
    # # llr.print()

    # llr.remove_at(1)
    # llr.print()

    # llr.insert_values(["banana","mango","grapes","orange"])
    # llr.print()


