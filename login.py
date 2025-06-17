from tkinter import * 
root=Tk()
root.title("login")
root.geometry("300x300")

frame= Frame(root,bg="red",relief=RAISED,borderwidth=5)
frame.pack()

label1= Label(frame,bg="green",text="Enter your name")
label1.pack()

entry1= Entry(frame)
entry1.pack()

root.mainloop()
