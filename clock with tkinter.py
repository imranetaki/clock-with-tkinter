import tkinter as tk
from time import strftime

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

app = tk.Tk()
app.title("Digital Clock")
app.resizable('false', 'false')

label = tk.Label(app, font=('digital 7', 40, 'bold'), background='black', foreground='red')
label.pack(anchor='center')

time()
app.mainloop()