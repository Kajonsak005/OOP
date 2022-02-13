from Apartment import Apartment
from House import House
from Purchase import Purchase
from Rent import Rent


class HouseRental(House, Rent):

    def __init__(self, type, **data):
        super().__init__(**data)
        self.type = type

    def display(self):
        print("\n")
        print("Type:", self.type)
        House.display(self)
        Rent.display(self)

    @staticmethod
    def prompt_init(square_feet, num_bedrooms, num_bathrooms, garage, fenced_yard, furnished, rent):
        asset = {}
        house = House.prompt_init(
            square_feet, num_bedrooms, num_bathrooms, garage, fenced_yard)
        rent = Rent.prompt_init(furnished, rent)
        asset.update(house)
        asset.update(rent)
        return asset


class HousePurchase(House, Purchase):
    pass


class ApartmentPurchase(Apartment, Purchase):
    pass


class ApartmentRental(Apartment, Rent):
    pass
