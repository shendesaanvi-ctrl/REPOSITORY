class Library:
    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    def checkout(self):
        if self.available:
            self.available = False
            print("Book issued")
        else:
            print("Not available")

    def return_book(self):
        self.available = True
        print("Book returned")

    def display(self):
        print(self.book_name, "-", self.author, "-", "Available" if self.available else "Not Available")

# Example
book = Library("Python Basics", "John")
book.display()
book.checkout()
book.display()
