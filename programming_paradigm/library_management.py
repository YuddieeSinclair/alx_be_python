class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self.__is_checked_out = _is_checked_out

    def return_book(self):
        self.__is_checked_out = False

    def check_book(self):
        self.__is_checked_out = True




class Library:
    def __init__(self):
        self.__books = []


    def add_book(self, book):
        if isinstance(book, Book):
            self.__books.append(book)
    
    def check_out_book(self, title):
        for i in self.__books:
            if i.title == title:
                i.check_book()

    def return_book(self, title):
        for i in self.__books:
            if i.title == title:
                i.return_book()

    def list_available_books(self):
        for i in self.__books:
            if i._Book__is_checked_out == True:
                break
            print(f"{i.title} by {i.author}")
