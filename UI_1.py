import tkinter as tk

root = tk.Tk()
T = tk.Text(root, height=10, width=30)
T.pack()
T.insert(tk.END, "Welcome to Project")

def facedetect():
    MsgBox = tkinter.messagebox.askquestion('Emotion Dispatcher',"Do you wish to proceed?",icon = 'warning')
    if MsgBox == 'yes':
    	os.system('UI_2.py')
    else:
        root.destroy()
button1 = tkinter.Button (root, text='Continue',command=facedetect,bg='white',fg='black') 
canvas1.create_window(150, 150, window=button1)

tk.mainloop()
