from tkinter import *

window = Tk()
window.title("Show Photo")
window.geometry("800x600")

photo_gif = PhotoImage(file="dog.gif")
Label(window, image=photo_gif).pack()

window.mainloop()
