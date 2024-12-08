# viewport2.py is a rewrite of viewport.py,
# eventually replacing it. remove this comment
# when that is done.

# viewport.py is the main file, and entry point,
# of the Viewport application.

import sys, os # import system utils
from tkinter import * # import tkinter
from tkinter import filedialog # import filedialog
from PIL import ImageTk, Image # import PIL components
app = Tk() # define 'app' to be the Tk application app

# generate accurate path for application icon,
# by first splitting off the tail of the path,
head, tail = os.path.split(os.path.abspath(__file__))
# then replacing tail with 'icon.ico', then normalizing
icon_path = os.path.normpath(f'{head}/icon.ico')
# now apply the icon to Tk title bar,
try:
    # we use try because this isn't critical, it's just nice,
    # but some platforms may have issues with this
    app.iconbitmap(icon_path)
except Exception as error:
    print('Icon not applied.', error)
    pass

# define 'geo' to be the size of the app geometry;
# use half the width and height of the user's screen
geo = f'{round(app.winfo_screenwidth()/2)}x{round(app.winfo_screenheight()/2)}'
# then apply to app
app.geometry(geo)
# define 'display' as the Tk label;
# an element that will hold our image
display = Label(app, image=None)
# then pack this element
display.pack(anchor='center', expand=True)


# image.open takes roughly 0.3 seconds

import time


current_file = "imageset/leopard_sunlight.jpg"

start = time.time()
current_image = ImageTk.PhotoImage(Image.open(current_file))
end = time.time()

print('Image open time')
print(end - start)


def ideal_size(original, limit_x, limit_y):
    # unpack original (tuple) into x and y
    original_x, original_y = original
    # if the original is already within limits,
    if original_x <= limit_x and original_y <= limit_y:
        # new size stays the same as original
        return (original_x, original_y)
    else:
        # calculate new size with the same aspect ratio
        ratio = min(limit_x / original_x, limit_y / original_y)
        return (int(original_x * ratio), int(original_y * ratio))


# opened_image = Image.open(current_file)
# resize_size = ideal_size(opened_image.size, app.winfo_width(), app.winfo_height())
# resized_image = opened_image.resize(resize_size)
# current_image = ImageTk.PhotoImage(resized_image)
display.configure(image=current_image)



def open_image(event):
    pass

def update_size(event):
    pass

def navigate_next(event):
    pass

def navigate_previous(event):
    pass

def navigate_first(event):
    pass

def navigate_last(event):
    pass

def navigate_shuffle(event):
    pass

def navigate_refresh(event):
    pass



app.bind('<o>', open_image) # Keybind: O to open
app.bind('<s>', navigate_shuffle) # Keybind: S to shuffle
app.bind('<Right>', navigate_next) # Keybind: Right to next
app.bind('<d>', navigate_next) # Keybind: Right to next
app.bind('<a>', navigate_previous) # Keybind: A to previous
app.bind('<Left>', navigate_previous) # Keybind: Left to previous
app.bind('<j>', navigate_first) # Keybind: Jump to first
app.bind('<k>', navigate_last) # Keybind: Jump to last
app.bind('<r>', navigate_refresh) # Keybind: Refresh
app.bind('<Configure>', update_size) # Bind update_size to app adjustments

# with everything defined, now run the main app loop:
app.mainloop()