import tkinter as tk
import tkinter.font as tkFont


from .PaymentPage import *
from .ResidentPage import *
from .SelectOptionPage import *


class AppResident(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Asset catalog")

        # setting window size
        width = 800
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (MainPage, DisplayPage, SelectResidentPage, HousePage, ApartmentPage, SelectPayment, RentPage, PurchasePage):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F.__name__] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame('MainPage')

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        GLabel_576 = tk.Label(self)
        ft = tkFont.Font(family='Chalkboard SE Regular', size=28)
        GLabel_576["font"] = ft
        # GLabel_576["fg"] = "#333333"
        GLabel_576["fg"] = "#ffffff"
        GLabel_576["justify"] = "center"
        GLabel_576["text"] = "Agent ID 1"
        GLabel_576.place(x=0, y=0, width=800, height=81)

        GButton_551 = tk.Button(self)
        GButton_551["bg"] = "#efefef"
        ft = tkFont.Font(family='Chalkboard SE Regular', size=16)
        GButton_551["font"] = ft
        GButton_551["fg"] = "#000000"
        GButton_551["justify"] = "center"
        GButton_551["text"] = "ADD Resident"
        GButton_551["relief"] = "flat"
        GButton_551.place(x=320, y=160, width=165, height=60)
        GButton_551["command"] = self.button_add_resident

        GButton_820 = tk.Button(self)
        GButton_820["bg"] = "#efefef"
        ft = tkFont.Font(family='Chalkboard SE Regular', size=16)
        GButton_820["font"] = ft
        GButton_820["fg"] = "#000000"
        GButton_820["justify"] = "center"
        GButton_820["text"] = "Display Asset"
        GButton_820["relief"] = "flat"
        GButton_820.place(x=320, y=280, width=165, height=60)
        GButton_820["command"] = self.button_display

    def button_add_resident(self):
        self.controller.show_frame('SelectResidentPage')

    def button_display(self):
        self.controller.show_frame('DisplayPage')
