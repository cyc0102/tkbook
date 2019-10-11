from tkinter import *
from PIL import Image, ImageTk
import cv2
# Create a window
tk = Tk()
# Load an image using OpenCV
cv_img = cv2.cvtColor(cv2.imread("dog.jpg"), cv2.COLOR_BGR2RGB)
# Get the image dimensions 
height, width, channels = cv_img.shape
# Create a canvas that can fit the above image
canvas = Canvas(tk, width = width+40 , height = height+30, bg="grey90")
#canvas = Canvas(tk, width=800, height=600, bg="yellow")
# Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
photo = ImageTk.PhotoImage(image = Image.fromarray(cv_img))
# Add a PhotoImage to the Canvas
canvas.create_image(20, 15, image=photo, anchor=NW) #anchor=NW North West or anchor=CENTER or ...
canvas.pack()
tk.mainloop()