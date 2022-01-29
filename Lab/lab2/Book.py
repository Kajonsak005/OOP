from Author import Author

class Book: 
    run_number = 1
    books = []

    def __init__(self,isbn,authors,title,subject,dds_number):

        self._id = Book.run_number

        check_isbn = Book.get_book_by_isbn(isbn)
        if len(check_isbn):
            raise Exception("ISBN "+isbn+" is duplicate")

        self.isbn = isbn
        self._authors = Author.find_id_by_list(authors)  
        self.title = title 
        self.subject = subject 
        self.dds_number = dds_number 

        Book.books.append(self)
        Book.run_number += 1

    @property
    def id(self):
        return self._id

    @property
    def authors(self):
        author_list = []
        for author in self._authors:
            author_list.append(Author.get_author_by_id(author))
        return author_list

    @authors.setter
    def authors(self,authors):
        if isinstance(authors,list):
            self.authors = Author.find_id_by_list(authors)
        print("set authors:",authors) 

    def delete(self):
        Book.books.remove(self)
        print("success! delete Book title: ",self.title)


    def get_book_by_title(name):
        books_list = []
        for book in Book.books:
            if name == book.title:
                books_list.append(book)
        return books_list  

    def get_book_by_subject(subject):
        books_list = []
        for book in Book.books:
            if subject == book.subject:
                books_list.append(book)
        return books_list

    def get_book_by_author(author_name):
        books_list = []
        for book in Book.books:
            for author_list in book.authors:
                if author_name == author_list.name:
                    books_list.append(book)
        return books_list

    def get_book_by_dds_number(dds_number):
        books_list = []
        for book in Book.books:
            if dds_number == book.dds_number:
                books_list.append(book)
        return books_list  

    def get_book_by_isbn(isbn):
        books_list = []
        for book in Book.books:
            if isbn == book.isbn:
                books_list.append(book)
        return books_list  

