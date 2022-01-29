from nis import cat
from Book import Book

class Catalog:

    ISBN = "ISBN"
    AUTHOR = "AUTHOR"
    TITLE = "TITLE"
    SUBJECT = "SUBJECT"
    DSS = "DSS"

    def __init__(self):
        pass

    def search(search_type,keyword):
        if search_type == Catalog.ISBN:
            book = Book.get_book_by_isbn(keyword)
            if not len(book):
                print("\nNot found:",keyword)
            return book
        elif search_type == Catalog.AUTHOR:
            book = Book.get_book_by_author(keyword)
            if not len(book):
                print("\nNot found:",keyword)
            return book
        elif search_type == Catalog.TITLE:
            book = Book.get_book_by_title(keyword)
            if not len(book):
                print("\nNot found:",keyword)
            return book
        elif search_type == Catalog.SUBJECT:
            book = Book.get_book_by_subject(keyword)
            if not len(book):
                print("\nNot found:",keyword)
            return book
        elif search_type == Catalog.DSS:
            book = Book.get_book_by_dds_number(keyword)
            if not len(book):
                print("\nNot found:",keyword)
            return book
        else :
            raise Exception("have problem search in search_type")