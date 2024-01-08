#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""
import tkinter as tk 
from tkinter import *
import math

win = tk.Tk()

eoutput = StringVar()
eoutput.set("Side c")

def clickFunction(event):
    print(event)
    n1 = float(e1.get())
    n2 = float(e2.get())
    x = n1**2 + n2**2
    answer = math.sqrt(x)
    a_entry.delete(0,END)
    a_entry.insert(0,answer)

l1 = Label(win, text="Enter side a:")
e1 = Entry(win, width=20)
l2 = Label(win, text="Enter side b:")
e2 = Entry(win, width=20)
b1 = Button(win, text="Click for side c")

b1.bind("<Button>",clickFunction)

a_label = Label(win, text="The length of side c is:")
a_entry = Entry(win, width=20, textvariable=eoutput)

l1.grid(row=1,column=1)
e1.grid(row=1,column=2)
l2.grid(row=2,column=1)
e2.grid(row=2,column=2)
b1.grid(row=3, column=1, columnspan=2)
a_label.grid(row=4,column=1)
a_entry.grid(row=4,column=2)

win.mainloop()