class Rental:

    def __init__(self, furnished, rent):
        self.furnished = furnished
        self.rent = rent

    def display(self):
        print("furnished:", self.furnished)
        print("rent:", self.rent)

    @staticmethod
    def prompt_init(furnished, rent):
        return {"furnished": furnished, "rent": rent}
