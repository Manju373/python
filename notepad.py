from tkinter import * 
from tkinter.filedialog import * 
root = Tk()
root.title("Notepad")

def openf():
    text.insert(END, open(askopenfilename()).read()) 

def savef():
    open(asksaveasfilename(defaultextension=".txt"),'w').write(text.get(1.0, END))


Button(root, text="Open", command=openf).pack()
Button(root, text="Save", command=savef).pack()

text = Text(root)
text.pack(expand=1, fill=BOTH)
root.mainloop()