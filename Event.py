from tkinter import * 
window = Tk()
window.title('Events')
window.geometry('500x500')
def keypress(event):
    print(event.char)
window.bind('<Key>',keypress)
def click (event):
    print("The button is successfully clicked")
button= Button(text="click me")
button.pack()
button.bind('<Button-1>',click)
window.mainloop()