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
all_files = [current_file]
current_file_index = 0


def grab_files(from_path):
    head, tail = os.path.split(from_path)
    folder = str(head)
    files = []
    for item in os.listdir(folder):
        for format in ['.png', '.jpg', '.jpeg', '.bmp', '.tif', '.gif', '.webp']:
            if item.endswith(format):
                item_path = folder + '/' + item
                files.append(item_path)
    print(files)
    return files, files.index(from_path)


def neat_name(file_path):
    head, tail = os.path.split(file_path)
    for format in ['.png', '.jpg', '.jpeg', '.bmp', '.tif', '.gif', '.webp']:
        tail = str(tail.replace(format, ''))
    return tail


def update():
    try:
        global current_image # we need this global
        current_file = all_files[current_file_index]
        window.title(neat_name(current_file))
        current_image = ImageTk.PhotoImage(Image.open(current_file))
        display.configure(image=current_image)
    except:
        print('Failed to load any image files')
        display.configure(image=None)


def open_folder(event):
    global current_file
    global all_files
    global current_file_index
    current_file = filedialog.askopenfilename()
    all_files, current_file_index = grab_files(current_file)
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
window.bind('<Right>', nxt)
window.bind('<Left>', prv)
window.bind('<r>', refresh)
update()
window.mainloop()