class Notebook:

    notes = []

    def __init__(self):
        pass

    def search(self, keyword):
        temp_note = []
        for note in self.notes:
            if note.match(keyword) == True:
                temp_note.append(note)
        return temp_note

    def new_note(self, note):
        self.notes.append(note)

    def modify_memo(self, id_book, memo):
        for note in self.notes:
            if note.id == id_book:
                note.memo = memo

    def modify_tag(self, id, tags):
        for note in self.notes:
            if note.id == id:
                note.tags = tags
