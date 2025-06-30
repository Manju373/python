import tkinter as tk

def calculate(): 
    p = float(principal.get())
    t = float(time.get())
    r = float(rate.get())
    si = (p * t * r)/ 100
    ci = p* ((1 + r/100) ** t) - p
    result.config(text="si: ${si:2f} ci: ${ci:.2f}")

root = tk.Tk()
root.title("Age calculator App")
root.geometry("400x400")

tk.Label(root, text="Principal").pack()
principal = tk.Entry(root)
principal.pack()

tk.Label(root, text="Time(years)").pack()
time = tk.Entry(root)
time.pack()

tk.Label(root, text="Rate (%)").pack()
rate = tk.Entry(root)
rate.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)
result = tk.Label(root, text="")
result.pack()

root.mainloop()
