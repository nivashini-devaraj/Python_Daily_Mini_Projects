class Library:
    def __init__(self):
        self.books = []  # list to store book names

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' added to the library.")

    def show_books(self):
        if len(self.books) == 0:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print("-", book)


# Derived Class (inherits from Library)
class Member(Library):
    def __init__(self):
        super().__init__()  # call the parent class (Library) constructor
        self.borrowed_books = []  

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            self.borrowed_books.append(book_name)
            print(f"You borrowed '{book_name}'.")
        else:
            print(f"Sorry, '{book_name}' is not available.")

    def return_book(self, book_name):
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            self.books.append(book_name)
            print(f"You returned '{book_name}'.")
        else:
            print(f"You didn't borrow '{book_name}'.")



lib_user = Member()

# Add books
lib_user.add_book("Harry Potter")
lib_user.add_book("The Jungle Book")

# View books
lib_user.show_books()

# Borrow a book
lib_user.borrow_book("Harry Potter")

# View after borrowing
lib_user.show_books()

# Return the book
lib_user.return_book("Harry Potter")

# View again
lib_user.show_books()
