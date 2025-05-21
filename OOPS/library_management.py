class Book:
    def __init__(self, book_id, title, author, is_available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = is_available
        self.borrowed_by = None

    def __str__(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by}"
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.borrowers = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        return f"Book '{book.title}' added to library"

    def remove_book(self, book_id):
        if book_id in self.books:
            book = self.books.pop(book_id)
            return f"Book '{book.title}' removed from library"
        return "Book not found"

    def borrow_book(self, book_id, borrower_name):
        if book_id not in self.books:
            return "Book not found"
        
        book = self.books[book_id]
        if not book.is_available:
            return "Book is already borrowed"
        
        book.is_available = False
        book.borrowed_by = borrower_name
        if borrower_name not in self.borrowers:
            self.borrowers[borrower_name] = []
        self.borrowers[borrower_name].append(book)
        return f"Book '{book.title}' borrowed by {borrower_name}"

    def return_book(self, book_id):
        if book_id not in self.books:
            return "Book not found"
        
        book = self.books[book_id]
        if book.is_available:
            return "Book is already in library"
        
        borrower = book.borrowed_by
        book.is_available = True
        book.borrowed_by = None
        self.borrowers[borrower].remove(book)
        return f"Book '{book.title}' returned by {borrower}"

    def list_available_books(self):
        available_books = [book for book in self.books.values() if book.is_available]
        return available_books

    def list_borrowed_books(self):
        borrowed_books = [book for book in self.books.values() if not book.is_available]
        return borrowed_books

# Example usage
if __name__ == "__main__":
    # Create a library
    library = Library("Central Library")
    
    # Add some books
    book1 = Book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("B002", "To Kill a Mockingbird", "Harper Lee")
    book3 = Book("B003", "1984", "George Orwell")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    # Perform some operations
    print(library.borrow_book("B001", "John"))
    print(library.borrow_book("B002", "Alice"))
    print(library.return_book("B001"))
    
    print("\nAvailable Books:")
    for book in library.list_available_books():
        print(book)
    
    print("\nBorrowed Books:")
    for book in library.list_borrowed_books():
        print(book) 