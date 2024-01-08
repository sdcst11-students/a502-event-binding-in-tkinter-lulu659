"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
import tkinter as tk 
from tkinter import *

def clickfunction(event):
    print(event)
    r1 = e1.get()
    r2 = e2.get()
    r3 = e3.get()
    a_entry.delete(0,END)
    a_entry.insert(0, f"Student name: {r1} \n student number: {r2} \n student grade: {r3}")

win = tk.Tk()

eoutput = StringVar()
eoutput.set("Student information")

l1 = Label(win, text = "Enter student name:")
e1 = Entry(win, width = 20)
l2 = Label(win, text = "Enter student number:")
e2 = Entry(win, width = 20)
l3 = Label(win, text = "Enter student grade:")
e3 = Entry(win, width = 20)
b1 = Button(win, text = "View student information")

b1.bind("<Button>", clickfunction)

a_label = Label(win, text="Student information:")
a_entry = Entry(win, width=75, textvariable=eoutput)

l1.grid(row=1,column=1)
e1.grid(row=1,column=2)
l2.grid(row=2,column=1)
e2.grid(row=2,column=2)
l3.grid(row=3,column=1)
e3.grid(row=3,column=2)
b1.grid(row=4, column=1, columnspan=2)

a_label.grid(row=5,column=1)
a_entry.grid(row=5,column=2)

win.mainloop()