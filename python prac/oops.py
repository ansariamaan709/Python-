class Book():
    def __init__(self,title,author,pages):
        self.title= title
        self.author= author
        self.pages = pages

    def __str__(self):
        return self.title
    def __repr__(self):
        return self.author

    def __len__(self):
        return self.pages
obj = Book('Python','Anonymous',200)
print(obj)
print(len(obj))
print(repr(obj))