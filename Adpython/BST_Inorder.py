class BinaryST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryST(data)
            
        else:
            if self.right:
                self.right.add_child(data)
            
            else:
                self.right = BinaryST(data)
    
    def in_order_transversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_transversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_transversal()
        
        return elements

    
    def search(self,val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if self.data < val:
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree(elements):
    root = BinaryST(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    numbers = [13,56,67,34,21,25,78]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_transversal())
    print(numbers_tree.search(45))