class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out  = False

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self._books.append(book)
        print("Added '{book.title}' by {book.author} to the library.")

    def check_out_book(self, title):
        for book in shelf._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    print("'{title}' is checked out.")
                    return
                else:
                    print("'{title}' is already checked out.")
                    return
        print("'{title}' was not found in the library.")
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out == False
                print("Successfullly returned '{title}'.")
                return
            else:
                print("'{title}' was not checked out.")
                return
        print("'{title}' was not found in the library.")

    def list_available_books(self):
        if available_books:
            for book in available_books:
                print("- '{book.title}' by {book.author}")
        else:
            print("No books are currently available.")