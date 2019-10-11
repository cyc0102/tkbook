from tkinter import *
def btn_hit():
    global msg_on
    if msg_on == False:
        msg_on = True
        x.set("顯示文字")
    else:
        msg_on = False
        x.set("")
window = Tk()
window.title("Global Variable")

msg_on = False
x = StringVar()

label = Label(window, textvariable=x,
              fg="blue", bg="lightyellow",
              font ="Verdana 16 bold",
              width=25, height=2).pack()
btn = Button(window, text="Hit", command=btn_hit).pack()
window.mainloop()              