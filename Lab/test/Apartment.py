from Property import Property


class Apartment(Property):

    def __init__(self, balcony, laundry, **data):
        Property.__init__(**data)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        Property.display(self)
        print("balcony:", self.balcony)
        print("laundry:", self.laundry)

    @staticmethod
    def prompt_init(balcony, laundry, **data):
        property_init = Property.prompt_init(**data)
        property_init.update({
            "balcony": balcony,
            "laundry": laundry,
        })
        return property_init
