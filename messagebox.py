from tkinter import *
from tkinter import messagebox

def myMsg():
    messagebox.showinfo("My Message Box", "Python 早安")

window = Tk()
window.title("My Window")
window.geometry("800x600")

Button(window, text="Good Morning", command=myMsg).pack()

window.mainloop()