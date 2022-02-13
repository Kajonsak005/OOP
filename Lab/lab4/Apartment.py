from Property import Property


class Apartment(Property):

    def __init__(self, balcony, laundry, **property):
        super().__init__(**property)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()

    @staticmethod
    def prompt_init(balcony, laundry, **property):
        dictionary = Property.prompt_init(**property)
        dictionary.update({"balcony": balcony})
        dictionary.update({"laundry": laundry})
        return dictionary
