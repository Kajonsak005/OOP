import tkinter as tk
from tkinter import *
import tkinter.font as tkFont


class SelectResidentPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        titile_lable = tk.Label(self)
        ft = tkFont.Font(family='Chalkboard SE Regular', size=28)
        titile_lable["font"] = ft
        # titile_lable["fg"] = "#333333"
        titile_lable["fg"] = "#ffffff"
        titile_lable["justify"] = "center"
        titile_lable["text"] = "Select Resident"
        titile_lable.place(x=0, y=0, width=800, height=81)

        button_house = tk.Button(self)
        button_house["bg"] = "#efefef"
        ft = tkFont.Font(family='Chalkboard SE Regular', size=16)
        button_house["font"] = ft
        button_house["fg"] = "#000000"
        button_house["justify"] = "center"
        button_house["text"] = "House"
        button_house["relief"] = "flat"
        button_house.place(x=150, y=200, width=165, height=60)
        button_house["command"] = self.button_house_command

        button_back = tk.Button(self)
        button_back["bg"] = "#efefef"
        ft = tkFont.Font(family='Chalkboard SE Regular', size=16)
        button_back["font"] = ft
        button_back["fg"] = "#000000"
        button_back["justify"] = "center"
        button_back["text"] = "Apartment"
        button_back["relief"] = "flat"
        button_back.place(x=480, y=200, width=165, height=60)
        button_back["command"] = self.button_back_command

    def button_house_command(self):
        self.controller.show_frame('HousePage')

    def button_back_command(self):
        self.controller.show_frame('AddResident')


class HousePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        titile_lable = tk.Label(self)
        ft = tkFont.Font(family='Chalkboard SE Regular', size=28)
        titile_lable["font"] = ft
        # titile_lable["fg"] = "#333333"
        titile_lable["fg"] = "#ffffff"
        titile_lable["justify"] = "center"
        titile_lable["text"] = "House"
        titile_lable.place(x=0, y=0, width=800, height=81)

        labels = []
        entries = []

        for index, label_list in enumerate(["square feet", "num bedrooms", "num bathrooms", "garage"]):

            entries.append(tk.Entry(self))
            entries[index] = tk.Entry(self)
            entries[index]["borderwidth"] = "1px"
            ft = tkFont.Font(family='Chalkboard SE Regular', size=16)
            entries[index]["font"] = ft
            entries[index]["fg"] = "#ffffff"
            entries[index]["justify"] = "center"
            entries[index]["text"] = "Entry"
            entries[index].place(x=340, y=(130+(index*30)),
                                 width=249, height=25)

            labels.append(tk.Label(self))
            ft = tkFont.Font(family='Chalkboard SE Regular', size=16)
            labels[index]["font"] = ft
            labels[index]["fg"] = "#ffffff"
            labels[index]["justify"] = "right"
            labels[index]["text"] = label_list
            labels[index].place(x=180, y=(130+(index*30)),
                                width=143, height=25)
        else:
            labels.append(tk.Label(self))
            index += 1
            ft = tkFont.Font(family='Chalkboard SE Regular', size=16)
            labels[index]["font"] = ft
            labels[index]["fg"] = "#ffffff"
            labels[index]["justify"] = "right"
            labels[index]["text"] = "fenced_yard"
            labels[index].place(x=180, y=(130+(index*30)),
                                width=143, height=25)

            GRadio_263 = tk.Radiobutton(
                self, text="Option 1")
            GRadio_263["font"] = ft
            GRadio_263["fg"] = "#ffffff"
            GRadio_263["justify"] = "center"
            GRadio_263.place(x=340, y=(130+(index*30)),
                             width=143, height=25)

            GRadio_47 = tk.Radiobutton(
                self, text="Option 2")
            GRadio_47["font"] = ft
            GRadio_47["fg"] = "#ffffff"
            GRadio_47["justify"] = "center"
            GRadio_47.place(x=440, y=(130+(index*30)),
                            width=143, height=25)


class ApartmentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
