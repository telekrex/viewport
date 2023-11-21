# testing image display with tkinter
from tkinter import *
from PIL import ImageTk, Image
f = './DCFC0689.JPG'
root = Tk()
root.geometry('500x500')
root.title('Imager')
frame = Frame(root)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open(f))
label = Label(frame, image = img)
label.pack()
root.mainloop()