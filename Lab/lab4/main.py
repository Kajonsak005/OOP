from Asset import *

type_map = {("house", "rental"): HouseRental,
            ("house", "purchase"): HousePurchase,
            ("apartment", "rental"): ApartmentRental,
            ("apartment", "purchase"): ApartmentPurchase}


def select_residence():
    while True:
        pass


def select_payment():
    while True:
        pass


while True:
    print("Please select option (number only)")
    print("1: Add apartment")
    print("2: Display asset")
    option = int(input("select option: "))

    if option == 1:
        pass
    elif option == 2:
        pass
