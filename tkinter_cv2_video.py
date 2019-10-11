from tkinter import *
import cv2 
from PIL import Image,ImageTk



def take_snapshot():
     print ( "snapshot press！" )

def video_loop():
     success, img = camera.read()   # 從攝像頭讀取照片
     if success: 
          cv2.waitKey( 100 )
          cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA) # 轉換顏色從BGR 到RGBA
          current_image = Image.fromarray(cv2image) # 將圖像轉換成Image 對象  
          imgtk = ImageTk.PhotoImage( image =current_image)
          label.imgtk = imgtk
          label.config( image =imgtk)
          tk.after( 1 , video_loop)


camera = cv2.VideoCapture(0)     # 攝像頭 
tk = Tk()


tk.title( "opencv + tkinter")   
label = Label(tk)
label.pack(padx =10, pady =10)






# label = Label(tk)   # initialize image panel

tk.config( cursor = "arrow" )
btn = Button(tk, text = " 點贊!" , command =take_snapshot)
btn.pack( fill = "both" , expand = True , padx = 10 , pady = 10 )

video_loop()

tk.mainloop()
# 當一切都完成後，關閉攝像頭並釋放所佔資源
camera.release()
cv2.destroyAllWindows()
