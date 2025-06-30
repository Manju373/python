from tkinter import * 
window = Tk()
window.title("Hotel System")
Label(window, text="Enter your quantity").pack(pady=5)
Label(window, text="pizza 159").pack()
e1=Entry(window)
e1.pack()
Label(window, text="french fries 140").pack()
e2=Entry(window)
e2.pack()
Label(window, text="burger 162").pack()
e3=Entry(window)
e3.pack()
Label(window, text="cold drink 40").pack()
e4=Entry(window)
e4.pack()
output=Label(window, text="Total 0")
output.pack(pady=10)

def calculate ():
    try:
        a=int(e1.get() or 0)
        b=int(e2.get() or 0)
        c=int(e3.get() or 0)
        d=int(e4.get() or 0)
        total = a*159+b*140+c*162+d*40
        output.config(text=f"Total {total}")
    except:
        output.config(text="invalid input")
Button(window, text="calculate total",command=calculate).pack(pady=5)
window.mainloop()