# On program launch,
# obtain: Image directory, Surrounding images, & Index of desired image
# then create the window to half the size of the user's monitor
# 
# Func: repeatable ------------------------------------------------------
# Set the background color to something close to the image
# Set the title of the window to the image file name
# Display the image
# -----------------------------------------------------------------------
# On L/R arrows, update to a new image
# ----------------------------------------------------------------------
#

import sys, os
from tkinter import *
from PIL import ImageTk, Image
window = Tk()
window.geometry('500x500') # !
frame = Frame(window)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)


OpenedImage = 'crab.png' # !
Directory = os.path.abspath(OpenedImage).replace(OpenedImage, '')
SurroundingImages = []
for file in os.listdir(Directory):
    for format in ['png', 'jpg', 'bmp']:
        if file.lower().endswith(format):
            SurroundingImages.append(str(Directory+file))
Index = SurroundingImages.index(Directory+OpenedImage)


window.title('Imager')
image = ImageTk.PhotoImage(Image.open(SurroundingImages[Index]))
label = Label(frame, image = image)
label.pack()




def display():
    global window
    global image
    global label
    global Index
    global SurroundingImages
    name = SurroundingImages[Index]
    window.title(SurroundingImages[Index])
    image = ImageTk.PhotoImage(Image.open(SurroundingImages[Index]))
    label = Label(frame, image = image)
    label.pack()


def inc():
    global Index
    global SurroundingImages
    if Index == len(SurroundingImages):
        Index = 0
    else:
        Index += 1
    display()


B = Button(frame, text ="Hello", command = inc)
B.pack()


display()
window.mainloop()