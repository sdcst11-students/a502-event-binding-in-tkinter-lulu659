"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk 
from tkinter import *
import math

win = tk.Tk()
eoutput = StringVar()
eoutput.set("Output goes here")

def clickFunction(event):
    print(event)
    b = float(e2.get())
    c = float(e3.get())
    answer = -b/2+math.sqrt((b/2)**2-c)
    answer1 = -b/2-math.sqrt((b/2)**2-c)
    a_entry.delete(0,END)
    a_entry.insert(0, f"The first x is {answer} and the second x is {answer1}.")

l1 = Label(win, text = "The program will factor a trinomial of the type ax^2 + bx + c. a is always 1.")
l2 = Label(win, text = "Enter b:")
e2 = Entry(win, width = 20)
l3 = Label(win, text = "Enter c:")
e3 = Entry(win, width = 20)
b1 = Button(win, text = "Factoring")
b1.bind("<Button>",clickFunction)

a_label = Label(win, text="The ax^2 - bx + c is:")
a_entry = Entry(win, width=75, textvariable=eoutput)

l1.grid(row = 1, column = 1, columnspan = 2)
l2.grid(row = 2, column = 1)
e2.grid(row = 2, column = 2)
l3.grid(row = 3, column = 1)
e3.grid(row = 3, column = 2)
b1.grid(row = 4, column = 1, columnspan = 2)
a_label.grid(row=5,column=1)
a_entry.grid(row=5,column=2)

win.mainloop()