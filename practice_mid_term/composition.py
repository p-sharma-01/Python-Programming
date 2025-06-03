class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []
    
    # Implement this
    def add_book(self, title, author):
        self.books.append([title,author])
    
    # Implement this
    def search_by_title(self, title):
        a=0
        for i in self.books:
            if title in i:
                a+=1
        if a==0:
            return False
        return True
                

# Test Input
lib = Library()
lib.add_book("1984", "George Orwell")
print(lib.search_by_title("1984"))  # Expected Output: True