class Catalog:

    ISBN = "ISBN"
    AUTHOR = "AUTHOR"
    TITLE = "TITLE"
    SUBJECT = "SUBJECT"
    DSS = "DSS"

    books = []

    def __init__(self):
        pass

    def add_book(book):
        Catalog.books.append(book)

    def delete_book(book):
        Catalog.books.remove(book)
        print("\nremove success !!")

    def search(search_type, keyword):
        temp_book = []
        if search_type == Catalog.ISBN:
            for book in Catalog.books:
                if book.isbn_match(keyword):
                    temp_book.append(book)
            return temp_book
        elif search_type == Catalog.AUTHOR:
            for book in Catalog.books:
                if book.author_match(keyword):
                    temp_book.append(book)
            return temp_book
        elif search_type == Catalog.TITLE:
            for book in Catalog.books:
                if book.title_match(keyword):
                    temp_book.append(book)
            return temp_book
        elif search_type == Catalog.SUBJECT:
            for book in Catalog.books:
                if book.subject_match(keyword):
                    temp_book.append(book)
            return temp_book
        elif search_type == Catalog.DSS:
            for book in Catalog.books:
                if book.dss_number_match(keyword):
                    temp_book.append(book)
            return temp_book
        else:
            raise Exception("have problem search in search type value")
