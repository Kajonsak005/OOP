from Property import Property


class House(Property):
    def __init__(self, garage='', fenced_yard='', **data):
        Property.__init__(self, **data)
        self.garage = garage
        self.fenced_yard = fenced_yard

    def display(self):
        Property.display(self)
        print("garage:", self.garage)
        print("fenced yard:", self.fenced_yard)

    @staticmethod
    def prompt_init(garage, fenced_yard, **data):
        property_init = Property.prompt_init(**data)
        property_init.update({
            "garage": garage,
            "fenced_yard": fenced_yard,
        })
        return property_init
