from library_management import Library, Book

def test_library():
    # Create a library
    library = Library("Test Library")
    
    # Create some books
    book1 = Book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("B002", "To Kill a Mockingbird", "Harper Lee")
    book3 = Book("B003", "1984", "George Orwell")
    
    # Test adding books
    print("Test 1: Adding Books")
    print(library.add_book(book1))
    print(library.add_book(book2))
    print(library.add_book(book3))
    print("Expected: Three success messages for adding books")
    print()
    
    # Test borrowing books
    print("Test 2: Borrowing Books")
    print(library.borrow_book("B001", "John"))
    print(library.borrow_book("B002", "Alice"))
    print("Expected: Two success messages for borrowing books")
    print()
    
    # Test borrowing unavailable book
    print("Test 3: Borrowing Unavailable Book")
    print(library.borrow_book("B001", "Bob"))
    print("Expected: Book is already borrowed")
    print()
    
    # Test returning book
    print("Test 4: Returning Book")
    print(library.return_book("B001"))
    print("Expected: Success message for returning book")
    print()
    
    # Test listing available books
    print("Test 5: Available Books")
    print("Available Books:")
    for book in library.list_available_books():
        print(book)
    print("Expected: Should show The Great Gatsby and 1984")
    print()
    
    # Test listing borrowed books
    print("Test 6: Borrowed Books")
    print("Borrowed Books:")
    for book in library.list_borrowed_books():
        print(book)
    print("Expected: Should show To Kill a Mockingbird")
    print()
    
    # Test removing book
    print("Test 7: Removing Book")
    print(library.remove_book("B003"))
    print("Expected: Success message for removing book")
    print()

if __name__ == "__main__":
    test_library() 