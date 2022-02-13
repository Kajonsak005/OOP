from Apartment import Apartment
from House import House
from Purchase import Purchase
from Rental import Rental


class HouseRental(House, Rental):

    def __init__(self, **data):
        House.__init__(self, **data["house"])
        Rental.__init__(self, **data["rental"])

    @staticmethod
    def prompt_init(garage, fenced_yard, square_feet, num_bedrooms, num_bathrooms, furnished, rent):
        house = House.prompt_init(
            garage, fenced_yard, square_feet, num_bedrooms, num_bathrooms)
        rental = Rental.prompt_init(furnished, rent)
        return {
            "house": house,
            "rental": rental
        }


class HousePurchase(House, Purchase):
    pass


class ApartmentPurchase(Apartment, Purchase):
    pass


class ApartmentRental(Apartment, Rental):
    pass
