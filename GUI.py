from Tkinter import *
import os
from PIL import ImageTk,Image
import Tkinter as Tk

class App:
    def __init__(self, master):
        master.minsize(width=110, height=110)
        self.frame = Frame(master)
        self.b = Button(self.frame, text = 'Open',bg="green",width=20,height=5, command = self.openFile)
        self.b.grid(row = 1)
        self.b.pack(side=LEFT)
        self.button = Button(self.frame, 
                         text="QUIT", fg="red",
                         command=self.close_window)
        self.button.pack(side=RIGHT)
        self.frame.grid()
    def openFile(self):
        os.startfile("run.bat")
    def close_window (self): 
     root.destroy()    



root = Tk.Tk()
background_image=Tk.PhotoImage(file="blind.gif")
background_label = Tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.wm_geometry("600x400+20+40")
root.title('IMAGE TO VOICE')

app = App(root)
root.mainloop()
    
