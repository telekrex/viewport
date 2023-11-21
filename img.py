import sys, os
from tkinter import *
from PIL import ImageTk, Image
# Initial tkinter setup boiler
window = Tk()
# Set the window size to start at 60%
# the size of the user's screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_size = f'{round(screen_width*.6)}x{round(screen_height*.6)}'
window.geometry(window_size)
# create the image frame, and set a
# fun cursor to use, because why not
frame = Frame(window, cursor='plus')
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)


# Open the image used to launch the program,
# then gather the surrounding images in the
# same directory. Max of 50 images though.
OpenedImage = 'crab.png' # [!] Use hook
Directory = os.path.abspath(OpenedImage).replace(OpenedImage, '')
SurroundingImages = []
i = 0
for file in os.listdir(Directory):
    # Max of 50 because I'm not sure
    # how many images would bust the
    # program; just being safe.
    i += 1
    if i < 50:
        for format in ['png', 'jpg', 'jpeg', 'bmp']:
            if file.lower().endswith(format):
                SurroundingImages.append(str(Directory+file))
# Now set the index of where we are to the original image
# file used to launch the program, so it starts there.
Index = SurroundingImages.index(Directory+OpenedImage)


# Create the image frame
window.title('Imager')
image = ImageTk.PhotoImage(Image.open(SurroundingImages[Index]))
label = Label(frame, image = image)
label.pack()


def display():
    global window
    global image
    global label
    global Index
    global Directory
    global SurroundingImages
    # Set the window title to the name of the file;
    # We get that from the path in the SurroundingImages list,
    # minus the Directory, which we get from the original opening
    window.title(SurroundingImages[Index].replace(Directory, ''))
    # Set the image to the new image
    image = ImageTk.PhotoImage(Image.open(SurroundingImages[Index]))
    label.configure(image=image)
    # [!] Then we need to resize the image to fit within the window


def inc():
    # incriment the current index to +1,
    # looping back to 0 if over, then
    # calling update()
    global Index
    global SurroundingImages
    if Index == len(SurroundingImages)-1:
        Index = 0
    else:
        Index += 1
    display()


def dec():
    # incriment the current index to -1,
    # looping back to max if under, then
    # calling update()
    global Index
    global SurroundingImages
    if Index == 0:
        Index = len(SurroundingImages)-1
    else:
        Index -= 1
    display()


B = Button(frame, text =">", command = inc)
B.pack()

C = Button(frame, text ="<", command = dec)
C.pack()


display()
window.mainloop()