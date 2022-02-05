from Book import Book
from Catalog import Catalog

defaultBooks = [["8858757423038", "XACT - TINMAN", "นิทาน fable", "บ้านฟักทองแสนสุข", "A1"],
                ["8858757423007", "XACT - TINMAN",
                    "นิทาน myth", "ต้นไม้เค้กมหัศจรรย์", "A2"],
                ["8858757423021", "XACT - TINMAN",
                    "นิทาน animal", "ปลาหมึกน้อยนักคำนวน", "A3"],
                ["9786161843809",
                    "Javis (จาร์วิส)", "Javis (จาร์วิส)", "ความลับของอลัน", "A4"],
                ["9786161845551", "Javis (จาร์วิส)",
                 "นิทาน ghost", "เด็กชายผมดอกไม้", "A5"],
                ["9786160453528", "Rikako Matsuo (ริกะโกะ มะสึโอะ)",
                 "นิทาน legend", "ของขวัญจากล็อตต้า", "A6"],
                ["9786167786490", "XACT - TINMAN",
                    "นิทาน explanatory", "นาฬิกาในป่าใหญ่", "A7"],
                ["9786167786483", "XACT - TINMAN",
                    "นิทาน jataka", "สร้ายคอของหนามแหลม", "A8"],
                ["9786167786698", "พรรณรวี ชัยอิ่นคำ,พรรณรวี,เอียมสม",
                    "นิทาน jest", "สามสหายผจญภัย", "A9"],
                ["9786167786650", "พรรณรวี ชัยอิ่นคำ", "นิทาน religious", "สุขสันต์วันเกิด", "A10"]]

for defaultBook in defaultBooks:
    Catalog.add_book(Book(defaultBook[0], defaultBook[1],
                          defaultBook[2], defaultBook[3], defaultBook[4]))


def displayBook(book):
    print("\nBook ISBN:", book.isbn)
    print("Book title:", book.title)
    print("Book author", ', '.join(
        [str(author_name.name)for author_name in book.authors]))
    print("Book subject:", book.subject)
    print("Book dds_number:", book.dds_number)


def addBook():
    isbn = input("isbn: ")
    author = input("author: ")
    title = input("title: ")
    subject = input("subject: ")
    dds_number = input("dds_number: ")
    Catalog.add_book(Book(isbn, author, title, subject, dds_number))
    print("\nadd book success")


def deleteBook():
    while (1):

        print("\nDelete Book:")
        print("1. Delete By isbn")
        print("2. Delete By title")
        print("0. Back to home")

        option = int(input("Action: "))

        # delete by isbn
        if option == 1:
            isbn_name = input("isbn name: ")
            Books = Catalog.search(Catalog.ISBN, isbn_name)
            for book in Books:
                Catalog.delete_book(book)
        # delete by title
        elif option == 2:
            title_name = input("title name: ")
            Books = Catalog.search(Catalog.TITLE, title_name)
            for book in Books:
                Catalog.delete_book(book)
        elif option == 0:
            break
        else:
            print("\ntry agin !!!")


def search_book():
    while (1):
        print("\n\nSearch Book:")
        print("1. Search by ISBN")
        print("2. Search by author")
        print("3. Search by title")
        print("4. Search by subject")
        print("5. Search by DSS number")
        print("6. Search All Books")
        print("0. Back")

        option = int(input("Action: "))

        if option == 1:
            title_name = input("ISBN : ")
            Books = Catalog.search(Catalog.ISBN, title_name)
            for book in Books:
                displayBook(book)
        elif option == 2:
            author_name = input("author name: ")
            Books = Catalog.search(Catalog.AUTHOR, author_name)
            print("\n")
            for book in Books:
                displayBook(book)
        elif option == 3:
            author_name = input("title name: ")
            Books = Catalog.search(Catalog.TITLE, author_name)
            print("\n")
            for book in Books:
                displayBook(book)
        elif option == 4:
            author_name = input("subject name: ")
            Books = Catalog.search(Catalog.SUBJECT, author_name)
            print("\n")
            for book in Books:
                displayBook(book)
        elif option == 5:
            author_name = input("DSS number name: ")
            Books = Catalog.search(Catalog.DSS, author_name)
            print("\n")
            for book in Books:
                displayBook(book)
        # display all
        elif option == 6:
            for book in Catalog.books:
                displayBook(book)
        elif option == 0:
            break
        else:
            print("\ntry agin !!!")


while (1):

    try:
        print("\n\nPlease select option (number Only):")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("0. Exit")

        option = int(input("Action: "))

        if option == 1:
            addBook()
        elif option == 2:
            deleteBook()
        elif option == 3:
            search_book()
        elif option == 0:
            exit()
        else:
            print("\n---try agin---")

    except Exception as error:
        print("\nsomthing is wrong !!!!\n")
        print(error)
        print("\n---try agin---")
