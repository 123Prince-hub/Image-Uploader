import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import PIL
import os
import random
from datetime import datetime 

root = tk.Tk()
root.minsize(600, 450)  # Size of the window 
root.maxsize(600, 450)  # Size of the window 
root.title('Prince Kirad')
my_font1=('times', 20, 'bold')
 
l1 = tk.Label(root, text ='Upload Your Photo',font=my_font1).place(relx = 0.5, rely = 0.1, anchor = 'center')
b1 = tk.Button(root, text="Upload Image",command = lambda:upload_file()).place(x=200, y=60)
b2 = tk.Button(root, text="Save Image",command = lambda:img_save()).place(x=300, y=60)

def upload_file():
    global img
    global filename
    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png'),('Jpeg Files', '*jpeg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    pic = Image.open(filename)
    resized_image= pic.resize((400,300), Image.ANTIALIAS)
    frame = Frame(root, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.6)
    new_image= ImageTk.PhotoImage(resized_image)
    label = Label(frame, image = new_image)
    label.pack()

def img_save():
    global filename
    pic = Image.open(filename)
    filepath = list(os.path.splitext(pic.filename))
    name = filepath[-2].split("/")
    name = name[-1]
    ext = filepath[-1]
    file = name+" "+datetime.now().strftime("%Y-%m-%d %I-%M-%S")
    pic.save(f"media/{file}{ext}")

root.mainloop()  # Keep the window open

