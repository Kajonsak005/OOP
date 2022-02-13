from datetime import datetime


class Note:

    note_id = 0

    def __init__(self, memo, tags):
        self.id = Note.note_id
        self.memo = memo
        self.tags = tags.split(",")
        now = datetime.now()
        self.creation_date = now.strftime("%m/%d/%Y")
        Note.note_id += 1

    def match(self, tag_or_memo):
        for tag in self.tags:
            if tag.find(tag_or_memo) >= 0:
                return True
        if self.memo.find(tag_or_memo) >= 0:
            return True
        return False
