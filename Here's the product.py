from tkinter import *
window = Tk()
window.title("Getting started with Widgets")
window.geometry("400x300")
label = Label(text ="Enter your name",bg="light blue",fg="black")
label.pack()
entry=Entry()
entry.pack()
def function():
    name = entry.get()
    textbox.insert(END,name)
button1=Button(text="click me",bg="light blue",fg="black",command=function)
button1.pack()
textbox=Text()
textbox.pack()
window.mainloop()