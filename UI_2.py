from tkinter import *

# pip install pillow
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("Learn-Facial-Recognition-scaled.jpg")
        load = load.resize((100,100),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=500, y=0)

        
root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("600x500")
root.mainloop()
