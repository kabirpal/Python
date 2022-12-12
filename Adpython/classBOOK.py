class Book:

    def __init__(self,Title,Author,Pages):
        self.Title = Title
        self.Author = Author
        self.Pages = Pages

    def __str__(self):
        return "Title: {}    Author: {}     Pages: {}".format(self.Title,self.Author,self.Pages)
    
    def __len__(self):
        return self.Pages

    def __del__(self):
        print("The book has been deleted successfully")   

b = Book("Monk who sold his ferari","Robin Sharma",890)
print(b.Author)
print(b.Title)
print(b.Pages)
print(b)
print(len(b))
del b
