from Menu import Menu

while True:
    try:
        print("\n\nPlease select option (number only)")
        print("1. Add note")
        print("2. Search")
        print("3. Modify note")
        print("4. Modify tags")
        print("5. Show note")
        print("0. Exit")

        option = int(input("Option: "))
        if option == 1:
            Menu.add_note()
        elif option == 2:
            Menu.search_note()
        elif option == 3:
            Menu.modify_note()
        elif option == 4:
            Menu.modify_tags()
        elif option == 5:
            Menu.show_note()
        elif option == 0:
            Menu.exit()

    except Exception as error:
        print("\nsomthing is wrong !!!!\n")
        print(error)
        print("\n---try agin---")
