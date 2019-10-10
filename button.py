from tkinter import *
def msgShow():
    label["text"]="文字中文顯示"
    label["bg"]="lightyellow"
    label["fg"]="blue"

window = Tk()
window.title("Button Example")    
label = Label(window)
btn = Button(window, text="Show Message",command=msgShow)

label.pack()
btn.pack()

window.mainloop()
