import sys, os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
window = Tk()
width = window.winfo_screenwidth() * .6
height = window.winfo_screenheight() * .6
size = f'{round(width)}x{round(height)}'
window.geometry(size)


current_file = "C:/Users/nitro/Documents/GitHub/image-viewer/Test Images/crab.png"
current_image = ImageTk.PhotoImage(Image.open(current_file))


display = Label(window, image=None)
display.pack(anchor='center', expand=True)


def update():
    window.title(current_file)
    display.configure(image=current_image)





update()




window.mainloop()