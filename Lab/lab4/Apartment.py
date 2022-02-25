from Property import Property


class Apartment(Property):

    def __init__(self, balcony, laundry, **data):
        Property.__init__(**data)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        Property.display(self)
        print("balcony:", self.balcony, "\nlaundry:", self.laundry)

    @staticmethod
    def prompt_init(balcony, laundry, **data):
        property_init = Property.prompt_init(**data)
        return {**property_init, "balcony": balcony, "laundry": laundry, }
