# a generic example of tk's performance
# used for understanding some bugs/perf

import sys, os
import subprocess
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from random import randrange
window = Tk()

width = window.winfo_screenwidth() * .6
height = window.winfo_screenheight() * .6
size = f'{round(width)}x{round(height)}'
window.geometry(size)
# window.configure(background='white')
display = Label(window, image=None)
display.pack(anchor='center', expand=True)

window.mainloop()