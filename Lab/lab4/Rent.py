class Rent:

    def __init__(self, furnished=False, rent=''):
        self.furnished = furnished
        self.rent = rent

    def display(self):
        print("furnished:", self.furnished, "\nrent:", self.rent)

    @staticmethod
    def prompt_init(furnished, rent):
        return {
            "furnished": furnished,
            "rent": rent
        }
