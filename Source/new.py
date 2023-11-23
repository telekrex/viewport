import sys, os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
window = Tk()
width = window.winfo_screenwidth() * .6
height = window.winfo_screenheight() * .6
size = f'{round(width)}x{round(height)}'
window.geometry(size)
display = Label(window, image=None)
display.pack(anchor='center', expand=True)


current_file = "C:/Users/nitro/Documents/GitHub/image-viewer/Test Images/crab.png"
current_image = ImageTk.PhotoImage(Image.open(current_file))


def update():
    global current_file
    global current_image
    window.title(current_file)
    current_image = ImageTk.PhotoImage(Image.open(current_file))
    display.configure(image=current_image)


def open_folder(event):
    global current_file
    current_file = filedialog.askopenfilename()
    update()


def nxt(event):
    print('next!')


def prv(event):
    print('previous!')


def refresh(event):
    update()


window.bind('<o>', open_folder)
window.bind('<Right>', nxt)
window.bind('<Left>', prv)
window.bind('<r>', refresh)
update()
window.mainloop()