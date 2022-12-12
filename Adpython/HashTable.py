#implementing a hashtable(which is also known as dictionary in python)

class Hashtable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
        h = self.get_hash(key) 
        return self.arr[h]

t = Hashtable()
t['march 6'] = 78
t['april 9'] = 67
t['jan 31'] = 28
t['feb 4'] = 71
t['oct 12'] = 98

print(t['oct 12'])