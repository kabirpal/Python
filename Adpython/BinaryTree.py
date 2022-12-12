class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)   
            else:
                self.left = BinaryTree(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTree(data)
    
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def InOrdertraversal(self):
        element = []

        if self.left:
            element += self.left.InOrdertraversal()

        element.append(self.data) 

        if self.right:
            element += self.right.InOrdertraversal()

        return element

def built_tree(element):
    root = BinaryTree(element[0])
    for i in range(1,len(element)):
        root.add_child(element[i])

    return root

if __name__ == '__main__':
    numbers = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    numbers_tree = built_tree(numbers)
    print(numbers_tree.InOrdertraversal())