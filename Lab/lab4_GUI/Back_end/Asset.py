from Apartment import Apartment
from House import House
from Purchase import Purchase
from Rent import Rent


class HouseRental(House, Rent):

    def __init__(self, **data):
        super().__init__(**data)

    def display(self):
        House.display(self)
        Rent.display(self)

    @staticmethod
    def prompt_init(square_feet, num_bedrooms, num_bathrooms, garage, fenced_yard, furnished, rent):
        house = House.prompt_init(square_feet, num_bedrooms, num_bathrooms, garage, fenced_yard)
        rent = Rent.prompt_init(furnished, rent)
        return {**house, **rent}


class HousePurchase(House, Purchase):
    def __init__(self, **data):
        super().__init__(**data)

    def display(self):
        print("\n")
        print("Type:", self.type)
        House.display(self)
        Purchase.display(self)

    @staticmethod
    def prompt_init(square_feet, num_bedrooms, num_bathrooms, garage, fenced_yard, price, taxes):
        house = House.prompt_init(
            square_feet, num_bedrooms, num_bathrooms, garage, fenced_yard)
        purchase = Purchase.prompt_init(price, taxes)
        return {**house, **purchase}


class ApartmentPurchase(Apartment, Purchase):
    def __init__(self, **data):
        super().__init__(**data)

    def display(self):
        Apartment.display(self)
        Rent.display(self)

    @staticmethod
    def prompt_init(balcony, laundry, square_feet, num_bedrooms, num_bathrooms, price, taxes):
        apartment = Apartment.prompt_init(
            balcony, laundry, square_feet, num_bedrooms, num_bathrooms)
        purchase = Purchase.prompt_init(price, taxes)
        return {**apartment, **purchase}


class ApartmentRental(Apartment, Rent):
    def __init__(self,  **data):
        super().__init__(**data)

    def display(self):
        House.display(self)
        Rent.display(self)

    @staticmethod
    def prompt_init(balcony, laundry, square_feet, num_bedrooms, num_bathrooms, furnished, rent):
        apartment = Apartment.prompt_init(
            balcony, laundry, square_feet, num_bedrooms, num_bathrooms)
        rent = Rent.prompt_init(furnished, rent)
        return {**apartment, **rent}
