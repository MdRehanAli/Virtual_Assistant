#tkinter is a GUI of python
from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title('Virtual Assistant')
root.geometry('520x320')

img = ImageTk.PhotoImage(Image.open('Assistant.jpg'))
panel = Label(root, image=img)
panel.pack(side='right', fill='both', expand='no')


root.mainloop()