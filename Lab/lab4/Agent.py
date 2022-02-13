from Asset import *


class Agent:

    def __init__(self):
        self.property_list = []

    def list_property(self):
        for _ in self.property_list:
            print("Property:", "")

    def add_property(self):
        pass


data = {
    "house": {
        "garage": 1,
        "fenced_yard": 2,
        "square_feet": 3,
        "num_bedrooms": 4,
        "num_bathrooms": 5,
    },
    "rental": {
        "furnished": 10,
        "rent": 20,
    }
}


instance = HouseRental(**data)
instance.display()
