from tkinter import *

window = Tk()
window.title("Show Photo")
window.geometry("800x600")

photo_gif = PhotoImage(file="dog.gif")
Label(window, image=photo_gif).pack(side="left")
photo_png = PhotoImage(file="dog.png")
Label(window, image=photo_png).pack(side="right")
window.mainloop()
