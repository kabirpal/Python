class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None


    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_data(self):
        print(self.data)
        for child in self.children():
            print(child.data)

def built_product_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Windows'))
    laptop.add_child(TreeNode('Linux'))

    mobiles = TreeNode('Mobiles')
    mobiles.add_child(TreeNode('Samsung'))
    mobiles.add_child(TreeNode('Apple'))
    mobiles.add_child(TreeNode('Vivo'))
    mobiles.add_child(TreeNode('Motorola'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('Samsung TV'))
    tv.add_child(TreeNode('LG'))

    root.add_child(laptop)
    root.add_child(mobiles)
    root.add_child(tv)

    return root

if __name__ == '__main__':
    root = built_product_tree()
    root.print_data()
    pass

