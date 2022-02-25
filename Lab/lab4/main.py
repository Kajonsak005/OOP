from Agent import Agent
from Asset import *


type_map = {("house", "rental"): HouseRental,
            ("house", "purchase"): HousePurchase,
            ("apartment", "rental"): ApartmentRental,
            ("apartment", "purchase"): ApartmentPurchase}


agent = Agent()


def input_property():
    return (input("square feet: "), input("num bedrooms: "), input("num bathrooms: "))


def input_house():
    print("\nHouse info")
    square_feet, num_bedrooms, num_bathrooms = input_property()
    garage = input("garage: ")
    fenced_yard = input("fenced_yard: ")
    return House.prompt_init(square_feet=square_feet, num_bedrooms=num_bedrooms, num_bathrooms=num_bathrooms, garage=garage, fenced_yard=fenced_yard)


def input_apartment():
    print("\nApartment info")
    prop = input_property()
    apartment = {
        "balcony": input("balcony: "),
        "laundry": input("laundry: ")
    }
    return {**apartment, **prop}


def input_rent():
    print("Rental info")
    return {
        "furnished": input("furnished (yes or no): "),
        "rent": input("rent: ")
    }


def input_purchase():
    print("purchase")
    return {
        "price": input("price: "),
        "taxes": input("taxes: ")
    }


def select_residence():
    while True:
        print("\nPlease select resident\n1: House\n2: Apartment")
        select = int(input("Select Option:"))
        if select == 1:
            info = input_house()
            return ("house", info)
        elif select == 2:
            info = input_apartment()
            return ("apartment", info)
        else:
            print("\ntry agin")


def select_payment():
    while True:
        print("\nPlease select payment\n1: Rent\n2: Purchase")
        select = int(input("Select Option:"))
        if select == 1:
            info = input_rent()
            return ("rental", info)
        elif select == 2:
            info = input_purchase()
            return ("purchase", info)
        else:
            print("try agin")


while True:
    print("\nPlease select option (number only)")
    print("1: Add resident")
    print("2: Display all resident")
    option = int(input("select option: "))

    if option == 1:
        resident, resident_info = select_residence()
        payment, payment_info = select_payment()
        type = {"type": resident+" "+payment}

        class_select = type_map[(resident, payment)]
        resident = class_select(**{**resident_info, **payment_info, **type})
        agent.add_property(resident)
    elif option == 2:
        agent.list_property()
