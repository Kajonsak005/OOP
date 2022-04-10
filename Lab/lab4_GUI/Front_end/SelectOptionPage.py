import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from turtle import width   # from x import * is bad practice


class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set, width=660, height=300)
        self.scrollable_frame.configure(bg="green")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


class DisplayPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        title_label = tk.Label(self)
        ft = tkFont.Font(family='Chalkboard SE Regular', size=28)
        title_label["font"] = ft
        title_label["fg"] = "#ffffff"
        title_label["justify"] = "center"
        title_label["text"] = "Display Resident"
        title_label.place(x=0, y=0, width=800, height=81)

        frame_display = tk.Frame(self, width=680, height=400, bg='green')
        frame_display.pack_propagate(0)
        frame_display.pack(side='top', padx=0, pady=100)

        # Todo list display object into for each

        frame = ScrollableFrame(frame_display)
        for i in range(50):
            Label(frame.scrollable_frame, text="ID: "+str(i), font=ft,
                  justify="left", width=30, anchor="w").pack()
            Label(frame.scrollable_frame, text="Num bathroom: "+str(i), font=ft,
                  justify="left", width=30, anchor="w").pack()
            Label(frame.scrollable_frame, text="Value: "+str(i), font=ft,
                  justify="left", width=30, anchor="w").pack()
            Label(frame.scrollable_frame, text="", font=ft,
                  justify="left", width=30, anchor="w").pack()

        frame.pack()

        button_back = tk.Button(self)
        button_back["bg"] = "#efefef"
        ft = tkFont.Font(family='Chalkboard SE Regular', size=16)
        button_back["font"] = ft
        button_back["fg"] = "#000000"
        button_back["justify"] = "center"
        button_back["text"] = "Back"
        button_back["relief"] = "flat"
        button_back.place(x=580, y=400, width=165, height=60)
        button_back["command"] = self.button_exit

    def button_exit(self):
        self.controller.show_frame('MainPage')
