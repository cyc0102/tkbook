from tkinter import *

flag=0
def msgShow():
    label1 = Label(window, text="Label 1 中文顯示", 
              bg="lightyellow", 
              width =15, 
              font="Helvetica 28 bold italic") 
    label1.pack(side=TOP)          
    
    label1.after(3000, label1.destroy)
    

window = Tk()
window.title("Button Example")  
window.geometry("800x600") 
#label = Label(window)
btn1 = Button(window, text="Show Message",width=15, command=msgShow)
btn2 = Button(window, text="Exit",width=15, command=window.destroy)

#label.pack()
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
window.mainloop()
