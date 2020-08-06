#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

window=Tk()

def km_to_miles():
    print(e1_value.get())
    gram=float(e1_value.get())*1000
    pound=float(e1_value.get())*2.20462
    ounce=float(e1_value.get())*35.274
    t1.delete("1.0", END)
    t1.insert(END,gram)
    t2.delete("1.0", END)
    t2.insert(END,pound)
    t3.delete("1.0", END)
    t3.insert(END,ounce)


l1=Label(window,text="KG")
l1.grid(row=0, column=0)


b1=Button(window,text="Convert", command=km_to_miles)
b1.grid(row=0,column=1)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=1, column=0)

l2=Label(window,text="Gram = ")
l2.grid(row=1, column=1)

l3=Label(window,text="Pound = ")
l3.grid(row=2,column=1)

l4=Label(window,text="Ounce = ")
l4.grid(row=3,column=1)

t1=Text(window, height=1, width=20)
t1.grid(row=1, column=2)

t2=Text(window, height=1, width=20)
t2.grid(row=2, column=2)

t3=Text(window, height=1, width=20)
t3.grid(row=3, column=2)

window.mainloop()