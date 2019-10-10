from tkinter import *
window = Tk()
window.title("My Window")
window.geometry("800x600")
label1 = Label(window, text="Label 1 中文顯示", 
              bg="lightyellow", 
              width =15, 
              font="Helvetica 28 bold italic") 
label2 = Label(window, text="Label 2 中文顯示", 
              bg="grey88", 
              width =15, 
              font="Helvetica 28 bold") 
label3 = Label(window, text="Label 3 中文顯示", 
              bg="snow", 
              width =15, 
              font="16")     
label4 = Label(window, text="Label 4 中文顯示", 
              bg="lightgreen", 
              width =15, 
              font="16") 
label5 = Label(window, text="Label 5 中文顯示", 
              bg="lightblue", 
              width =15, 
              font="16")              
label6 = Label(window, text="Label 6 中文顯示", 
              bg="snow2", 
              width =15, 
              font="16")      
label1.pack(side=TOP)
label2.pack(side=BOTTOM)
label3.pack(side=LEFT)
label4.pack(side=RIGHT)
label5.pack(side=RIGHT, padx=5)
label6.place(x=0,y=500)


window.mainloop()