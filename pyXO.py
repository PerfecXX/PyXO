"""
version 1.0B
Written by: Teeraphat Kullanankanjana
Computer Engineering Robotic and Technology: CERT
Thai-Nichi Institute of Technology, Thailand
"""

from tkinter import *
from tkinter import ttk, messagebox


def CheckWinner():
    global TurnCounter
    if TurnCounter > 5 < 10:
        Winner = GetColor(TurnCounter + 1)
        if ButtonState["Button1"] == ButtonState["Button2"] == ButtonState["Button3"] != 0:
            messagebox.showinfo(title="Winner", message="{} is winner".format(Winner))
            root.destroy()
        elif ButtonState["Button4"] == ButtonState["Button5"] == ButtonState["Button6"] != 0:
            messagebox.showinfo(title="Winner", message="{} is winner".format(Winner))
            root.destroy()
        elif ButtonState["Button7"] == ButtonState["Button8"] == ButtonState["Button9"] != 0:
            messagebox.showinfo(title="Winner", message="{} is winner".format(Winner))
            root.destroy()
        elif ButtonState["Button1"] == ButtonState["Button4"] == ButtonState["Button7"] != 0:
            messagebox.showinfo(title="Winner", message="{} is winner".format(Winner))
            root.destroy()
        elif ButtonState["Button2"] == ButtonState["Button5"] == ButtonState["Button8"] != 0:
            messagebox.showinfo(title="Winner", message="{} is winner".format(Winner))
            root.destroy()
        elif ButtonState["Button3"] == ButtonState["Button6"] == ButtonState["Button9"] != 0:
            messagebox.showinfo(title="Winner", message="{} is winner".format(Winner))
            root.destroy()
        elif ButtonState["Button1"] == ButtonState["Button5"] == ButtonState["Button9"] != 0:
            messagebox.showinfo(title="Winner", message="{} is winner".format(Winner))
            root.destroy()
        elif ButtonState["Button3"] == ButtonState["Button5"] == ButtonState["Button7"] != 0:
            messagebox.showinfo(title="Winner", message="{} is winner".format(Winner))
            root.destroy()
    if TurnCounter == 10:
        messagebox.showinfo(title="Winner", message="Game Tie")
        root.destroy()


def AddTurnCounter():
    global TurnCounter
    TurnCounter += 1
    if TurnCounter <= 10:
        TurnTitle.configure(text="Turn {}".format(TurnCounter))
    else:
        pass


def GetColor(TurnCounter):
    if TurnCounter % 2 == 0:
        return str("blue")
    else:
        return str("red")


def Click(Number):
    global TurnCounter
    Color = GetColor(TurnCounter)
    if Number == 1:
        if Color == "red":
            ButtonState["Button1"] = 1
        elif Color == "blue":
            ButtonState["Button1"] = 2
        Button1.configure(bg=Color, state="disable")
        AddTurnCounter()
    if Number == 2:
        if Color == "red":
            ButtonState["Button2"] = 1
        elif Color == "blue":
            ButtonState["Button2"] = 2
        Button2.configure(bg=Color, state="disable")
        AddTurnCounter()
    if Number == 3:
        if Color == "red":
            ButtonState["Button3"] = 1
        elif Color == "blue":
            ButtonState["Button3"] = 2
        Button3.configure(bg=Color, state="disable")
        AddTurnCounter()
    if Number == 4:
        if Color == "red":
            ButtonState["Button4"] = 1
        elif Color == "blue":
            ButtonState["Button4"] = 2
        Button4.configure(bg=Color, state="disable")
        AddTurnCounter()
    if Number == 5:
        if Color == "red":
            ButtonState["Button5"] = 1
        elif Color == "blue":
            ButtonState["Button5"] = 2
        Button5.configure(bg=Color, state="disable")
        AddTurnCounter()
    if Number == 6:
        if Color == "red":
            ButtonState["Button6"] = 1
        elif Color == "blue":
            ButtonState["Button6"] = 2
        Button6.configure(bg=Color, state="disable")
        AddTurnCounter()
    if Number == 7:
        if Color == "red":
            ButtonState["Button7"] = 1
        elif Color == "blue":
            ButtonState["Button7"] = 2
        Button7.configure(bg=Color, state="disable")
        AddTurnCounter()
    if Number == 8:
        if Color == "red":
            ButtonState["Button8"] = 1
        elif Color == "blue":
            ButtonState["Button8"] = 2
        Button8.configure(bg=Color, state="disable")
        AddTurnCounter()
    if Number == 9:
        if Color == "red":
            ButtonState["Button9"] = 1
        elif Color == "blue":
            ButtonState["Button9"] = 2
        Button9.configure(bg=Color, state="disable")
        AddTurnCounter()
    CheckWinner()


ButtonState = {'Button1': 0,
               'Button2': 0,
               'Button3': 0,
               'Button4': 0,
               'Button5': 0,
               'Button6': 0,
               'Button7': 0,
               'Button8': 0,
               'Button9': 0,
               }

TurnCounter = 1

root = Tk()
root.title("XO games")
root.resizable(0, 0)
root.wm_minsize(450, 400)

TurnTitle = Label(text="Turn 1", font=("TkDefaultFont", 20))
TurnTitle.place(x=180, y=0, height=50)

Button1 = Button(text="", command=lambda: Click(1))
Button1.place(x=100, y=100, width=80, height=80)

Button2 = Button(text="", command=lambda: Click(2))
Button2.place(x=180, y=100, width=80, height=80)

Button3 = Button(text="", command=lambda: Click(3))
Button3.place(x=260, y=100, width=80, height=80)

Button4 = Button(text="", command=lambda: Click(4))
Button4.place(x=100, y=180, width=80, height=80)

Button5 = Button(text="", command=lambda: Click(5))
Button5.place(x=180, y=180, width=80, height=80)

Button6 = Button(text="", command=lambda: Click(6))
Button6.place(x=260, y=180, width=80, height=80)

Button7 = Button(text="", command=lambda: Click(7))
Button7.place(x=100, y=260, width=80, height=80)

Button8 = Button(text="", command=lambda: Click(8))
Button8.place(x=180, y=260, width=80, height=80)

Button9 = Button(text="", command=lambda: Click(9))
Button9.place(x=260, y=260, width=80, height=80)

root.mainloop()
