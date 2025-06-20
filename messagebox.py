from tkinter import * 
from tkinter import messagebox

root =Tk()
root.geometry('200x200')

def msg():
    messagebox.showinfo("Alert", "Text to be displayed")
button = Button (root, text="click me", command=msg)
button.place(x=40, y=80)
root.mainloop()