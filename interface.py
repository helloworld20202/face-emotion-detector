import tkinter
import sys
import os
from tkinter import messagebox
root = tkinter.Tk()
canvas1 = tkinter.Canvas(root, width = 300, height = 300)
canvas1.pack()
def facedetect():
    MsgBox = tkinter.messagebox.askquestion('Emotion Dispatcher',"Do you wish to proceed?",icon = 'warning')
    if MsgBox == 'yes':
    	os.system('real_time_video.py')
    else:
        root.destroy()
button1 = tkinter.Button (root, text='Continue',command=facedetect,bg='white',fg='black') 
canvas1.create_window(150, 150, window=button1)
root.mainloop()
