from gettext import Catalog
from Author import Author
from Catalog import Catalog


class Book:
    def __init__(self, isbn, authors, title, subject, dds_number):

        check_isbn = Catalog.search(Catalog.ISBN, isbn)
        if len(check_isbn):
            raise Exception("ISBN "+isbn+" is duplicate")

        temp_author = []
        for author in authors.split(","):
            temp_author.append(Author(author))
        self.isbn = isbn
        self.authors = temp_author
        self.title = title
        self.subject = subject
        self.dds_number = dds_number

    def title_match(self, name):
        if name == self.title:
            return True
        return False

    def subject_match(self, subject):
        if subject == self.subject:
            return True
        return False

    def author_match(self, author_name):
        for author in self.authors:
            if author_name == author.name:
                return True
        return False

    def dds_number_match(self, dds_number):
        if dds_number == self.dds_number:
            return True
        return False

    def isbn_match(self, isbn):
        if isbn == self.isbn:
            return True
        return False
