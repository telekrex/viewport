# Written by telekrex

import sys, os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from random import randrange
window = Tk()
try:
    window.iconbitmap('icon.ico')
except:
    pass
width = window.winfo_screenwidth() * .6
height = window.winfo_screenheight() * .6
size = f'{round(width)}x{round(height)}'
window.geometry(size)
# window.configure(background='white')
display = Label(window, image=None)
display.pack(anchor='center', expand=True)

# To settle this open first image dispute, I'll just have to create a blank image,
# and have this part of the program get current working directory, use that path
# and image, then load that, and just wait for the user to press O.

current_file = ''.join(sys.argv[1:]) if len(sys.argv) > 1 else "NoImage.png"
current_image = ImageTk.PhotoImage(Image.open(current_file))
all_files = [current_file]
current_file_index = 0

def grab_files(from_path):
    head, tail = os.path.split(from_path)
    folder = str(head)
    files = []
    for item in os.listdir(folder):
        for format in ['.png', '.jpg', '.jpeg', '.bmp', '.tif', '.webp']:
            if item.endswith(format):
                item_path = folder + '/' + item
                files.append(item_path)
    print(files)
    return files, files.index(from_path)

def neat_name(file_path):
    head, tail = os.path.split(file_path)
    for format in ['.png', '.jpg', '.jpeg', '.bmp', '.tif', '.gif', '.webp']:
        tail = str(tail.replace(format, ''))
    return tail[:80]

def resized_image(original_size, limit_x, limit_y):
    # Unpack original size
    original_x, original_y = original_size
    # Calculate new size while maintaining aspect ratio
    if original_x <= limit_x and original_y <= limit_y:
        # Image already within limits
        new_size = (original_x, original_y)
    else:
        # Calculate new size with the same aspect ratio
        ratio = min(limit_x / original_x, limit_y / original_y)
        new_size = (int(original_x * ratio), int(original_y * ratio))
    return new_size

def update():
    try:
        global current_image # we need this global
        current_file = all_files[current_file_index]
        window.title(neat_name(current_file))
        # open image
        x = Image.open(current_file)
        # resize image to fit window
        zscale = resized_image((x.size), window.winfo_width(), window.winfo_height())        
        r = x.resize(zscale)
        # load that image as a ImageTk.PhotoImage
        current_image = ImageTk.PhotoImage(r)
        # current_image = ImageTk.PhotoImage(Image.open(current_file))
        display.configure(image=current_image)
    except Exception as e:
        print('Failed to load any image files')
        print(e)
        display.configure(image=None)

def open_folder(event):
    global current_file
    global all_files
    global current_file_index
    current_file = filedialog.askopenfilename()
    if current_file:
        all_files, current_file_index = grab_files(current_file)
        update()

def shuffle(event):
    global current_file_index
    global all_files
    current_file_index = randrange(len(all_files)-1)
    update()

def nxt(event):
    global current_file_index
    global all_files
    if current_file_index < len(all_files)-1:
        current_file_index += 1
    else:
        current_file_index = 0
    update()

def prv(event):
    global current_file_index
    global all_files
    if current_file_index == 0:
        current_file_index = len(all_files)-1
    else:
        current_file_index -= 1
    update()

def refresh(event):
    update()

window.bind('<o>', open_folder)
window.bind('<s>', shuffle)
window.bind('<Right>', nxt)
window.bind('<d>', nxt)
window.bind('<a>', prv)
window.bind('<Left>', prv)
window.bind('<r>', refresh)
window.bind('<Configure>', refresh) # This event gets called upon moving location or resizing window,
# so the refreshing is happening constantly -- this is a performance issue. But not one I really know
# how to fix at the moment.
update()
window.mainloop()