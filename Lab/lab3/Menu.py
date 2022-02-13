from Note import Note
from Notebook import Notebook


class Menu:

    note_book = Notebook()
    note_book.new_note(Note("memo", "tags"))
    note_book.new_note(Note("kong", "king,king,king,king"))
    note_book.new_note(Note("kong", "king"))
    note_book.new_note(Note("kong", "king"))
    note_book.new_note(Note("kong", "king"))

    def __init__(self):
        pass

    def show_note():
        for note in Menu.note_book.notes:
            print("\n\nId:", note.id)
            print("Memo:", note.memo)
            print("Tags:", ', '.join([str(tags)for tags in note.tags]))
            print("Creation date:", note.creation_date)

    def search_note():
        print("\n\nYou can search with multiple memo or tags.")
        print("please separated by \" , \"")
        keyword = input("Search: ")
        notes = Menu.note_book.search(keyword)
        for note in notes:
            print("\n\nId:", id(note))
            print("Memo:", note.memo)
            print("Tags:", note.tags)
            print("Creation date:", note.creation_date)

    def add_note():
        print("\n\nAdd Note: ")
        print("you can input multiple memo.  please separated by \" , \"")
        memo = input("Memo: ")
        print("you can input multiple tags.  please separated by \" , \"")
        tags = input("Tags: ")
        Menu.note_book.new_note(Note(memo, tags))

    def modify_note():
        print("\n\nModify memo: ")
        id_book = int(input("Id: "))
        print("you can input multiple tags.  please separated by \" , \"")
        memo = input("Memo: ").split(",")
        Menu.note_book.modify_memo(id_book, memo)

    def modify_tags():
        print("\n\nModify tags: ")
        id_book = int(input("Id: "))
        print("you can input multiple tags.  please separated by \" , \"")
        memo = input("Tags: ").split(",")
        Menu.note_book.modify_memo(id_book, memo)

    def exit():
        exit()
