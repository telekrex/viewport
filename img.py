import sys, os
from tkinter import *
from tkinter import filedialog
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



# x = filedialog.askopenfilename()
x = 'C:/Users/nitro/Documents/GitHub/image-viewer/crab.png'
head, tail = os.path.split(x)

# Open the image used to launch the program,
# then gather the surrounding images in the
# same directory. Max of 50 images though.
OpenedImage = tail
Directory = head
SurroundingImages = []
Index = 0
i = 0
for file in os.listdir(Directory):
    # Max of 50 because I'm not sure
    # how many images would bust the
    # program; just being safe.
    if i < 50:
        # this check ensures we
        # are not including folders
        # in our surrounding images
        if os.path.isfile(file):
            # now we are looking for just image files
            for format in ['png', 'jpg', 'jpeg', 'bmp']:
                if file.lower().endswith(format):
                    z = os.path.join(Directory, file)
                    SurroundingImages.append(z)
                    if file == tail:
                        # Now set the index of where we are to the original image
                        Index = i
i += 1
# I hate this loop so much, but that's how I got this working. I'll make it better.


# Create the image frame
# Yes, this gets entirely
# replaced in display(),
# but I can't think of
# any other way to go
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
    name = SurroundingImages[Index].replace(Directory, '')
    x = name.split('.')
    name = x[0]
    name = name.replace(r'/', '')
    name = name.replace(r'\\', '')
    # I swear to fuck I will get rid
    # of these slashes one fucking day
    window.title(name)
    # Set the image to the new image
    image = ImageTk.PhotoImage(Image.open(SurroundingImages[Index]))
    label.configure(image=image)
    # [!] Then we need to resize the image to fit within the window


def inc(event):
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


def dec(event):
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

def refresh(event):
    display()
    # print('refreshed')


# Bind the Right and Left arrow keys
# to the inc and dec functions
window.bind('<Right>', inc)
window.bind('<Left>', dec)
# Bind R to refresh display
window.bind('<r>', refresh)
# Init first display update
display()
# Run the loop
window.mainloop()