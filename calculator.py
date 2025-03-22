
from tkinter import *

win=Tk()

win.geometry('360x280')
win.title("Calculator")

#Button-Clicks

#operations

def click(num):
    entry.insert(END, str(num))  # Append number to entry field

def equal():
    expression = entry.get()  # Get the full expression (e.g., "5+3")
    try:
        result = eval(expression)  # Evaluate the mathematical expression
        entry.insert(END, " = " + str(result))  # Show result without clearing
    except:
        entry.insert(END, " Error")

def clear():
    entry.delete(0, END)

#Entry Box

entry=Entry(win,width=58, borderwidth=5,relief="ridge",bd=2)
entry.pack(pady=10, ipady=5)
entry.place(x=3, y=2)

#Buttons

button=Button(win,height=1,text="1", width=6, bg="black", fg="white", font=8, command=lambda :click(1))  #lambda: Creates an anonymous function (a function without a name).
button.place(x=5, y=50)                                                  #command parameter does not accept functions with arguments directly.This is where lambda comes in.

button=Button(win, height=1,text="2", width=6, bg="black", fg="white", font=8,command=lambda :click(2))
button.place(x=95, y=50)

button=Button(win, height=1,text="3", width=6, bg="black", fg="white", font=8,command=lambda :click(3))
button.place(x=185, y=50)

button=Button(win, height=1,text="+", width=6, bg="orange", fg="white", font=12,command=lambda :click("+"))
button.place(x=275, y=50)

button=Button(win, height=1,text="4", width=6, bg="black", fg="white", font=8,command=lambda :click(4))
button.place(x=5, y=100)

button=Button(win, height=1,text="5", width=6, bg="black", fg="white", font=8,command=lambda :click(5))
button.place(x=95, y=100)

button=Button(win, height=1,text="6", width=6, bg="black", fg="white", font=8,command=lambda :click(6))
button.place(x=185, y=100)

button=Button(win, height=1,text="-", width=6, bg="orange", fg="white", font=12,command=lambda :click("-"))
button.place(x=275, y=100)

button=Button(win, height=1,text="7", width=6, bg="black", fg="white", font=8,command=lambda :click(7))
button.place(x=5, y=150)

button=Button(win, height=1,text="8", width=6, bg="black", fg="white", font=8,command=lambda :click(8))
button.place(x=95, y=150)

button=Button(win, height=1,text="9", width=6, bg="black", fg="white", font=8,command=lambda :click(9))
button.place(x=185, y=150)

button=Button(win, height=1,text="*", width=6, bg="orange", fg="white", font=12,command=lambda :click("*"))
button.place(x=275, y=150)

button=Button(win, height=1,text="=", width=6, bg="orange", fg="white", font=8,command=equal)
button.place(x=5, y=200)

button=Button(win, height=1,text="clear", width=6, bg="orange", fg="white", font=6,command=clear)
button.place(x=95, y=200)

button=Button(win, height=1,text="0", width=6, bg="orange", fg="white", font=8,command=lambda :click(0))
button.place(x=185, y=200)

button=Button(win, height=1,text="/", width=6, bg="orange", fg="white", font=12,command=lambda :click("/"))
button.place(x=275, y=200)






win.mainloop()