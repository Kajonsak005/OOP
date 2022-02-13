class Rent:

    def __init__(self, furnished, rent, **data):
        super().__init__(**data)
        self.furnished = furnished
        self.rent = rent

    def display(self):
        print("furnished:", self.furnished)
        print("rent:", self.rent)

    @staticmethod
    def prompt_init(furnished, rent):
        return {
            "furnished": furnished,
            "rent": rent
        }
