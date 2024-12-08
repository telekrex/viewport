# viewportctk.py is a (maybe) rewrite of viewport.py because it's terrible


import sys, os # system utilities
from customtkinter import * # https://customtkinter.tomschimansky.com/documentation/
import tkinter as tk # apparently needed

# app window
app = CTk()
app.geometry("800x800")
app.title('Viewport')


# define a frame that
# holds all subs parts
main = CTkFrame(
    # parent to "app"
    master=app)
# then pack,
main.pack(
    fill=tk.BOTH, # fill the parent
    expand=True, # expand with resized,
    padx=10, pady=10 # and padding of 10px
    )

# define the footer frame,
# which holds keybind text
footer = CTkFrame(
    # parent to "app"
    master=app)
# then pack,
footer.pack(
    fill=tk.X,
    expand=True, # expand with resized,
    padx=10, pady=10 # and padding of 10px
    )


# run application
app.mainloop()