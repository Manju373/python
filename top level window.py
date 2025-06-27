from tkinter import * 
window=Tk()

window.title("main window")
window.geometry("500x500")
window.configure(bg="gray")
def toplevelwindow():
    top=Toplevel()
    top.title("Toplevelwindow")
    top.geometry("300x300")
    top.configure(bg="yellow")
    top.mainloop()
button=Button(window,text="select to open another window",command=toplevelwindow)
button.pack()
window.mainloop()