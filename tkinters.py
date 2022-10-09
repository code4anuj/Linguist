# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry(widthxheight)
root.geometry('350x200')

#adding a label to the root window
lbl = Label(root, text = "Are you a Geek?")
lbl.grid()

# Execute Tkinter
root.mainloop()
