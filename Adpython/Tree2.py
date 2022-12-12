class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        #self has been defined as parent
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_data(self):
        space = " " * self.get_level() * 5
        prefix = space + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_data()

def built_the_child():
    root = TreeNode('KB Tuition Center')

    class7 = TreeNode('Class 7th')
    class7.add_child(TreeNode('Aditiya'))

    class1 = TreeNode('Class 1st')
    class1.add_child(TreeNode('Keshav'))
    
    class2 = TreeNode('Class 2nd')
    class2.add_child(TreeNode('Swayam'))
    
    class3 = TreeNode('Class 3rd')
    class3.add_child(TreeNode('Jeet'))
    class3.add_child(TreeNode('Harsh'))
    
    class4 = TreeNode('Class 4th')
    class4.add_child(TreeNode('Ronak'))
    class4.add_child(TreeNode('Devant'))
    
    class5 = TreeNode('Class 5th')
    class5.add_child(TreeNode('Piyu'))
    
    class8 = TreeNode('Class 8th')
    class8.add_child(TreeNode('Tuni'))
    class8.add_child(TreeNode('Khushi'))

    root.add_child(class1)
    root.add_child(class2)
    root.add_child(class3)
    root.add_child(class4)
    root.add_child(class5)
    root.add_child(class7)
    root.add_child(class8)

    root.print_data()

if __name__ == '__main__':
    built_the_child()