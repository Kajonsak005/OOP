from Property import Property


class House(Property):

    def __init__(self, garage, fenced_yard, **property):
        super().__init__(**property)
        self.garage = garage
        self.fenced_yard = fenced_yard

    def display(self):
        Property.display(self)
        print("garage:", self.garage)
        print("fenced_yard:", self.fenced_yard)

    @staticmethod
    def prompt_init(garage, fenced_yard, **property):
        dictionary = Property.prompt_init(**property)
        dictionary.update({"garage": garage})
        dictionary.update({"fenced_yard": fenced_yard})
        return dictionary
