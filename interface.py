#tkinter is a GUI of python
from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title('Virtual Assistant')
#root.geometry('520x320')

img = ImageTk.PhotoImage(Image.open('Assistant.jpg'))
panel = Label(root, image=img)
panel.pack(side='right', fill='both', expand='no')

userText = StringVar()

userText.set('Your Virtual Assistant')
userFrame = LabelFrame(root, text='Lena', font=('Railways', 24, 'bold'))
userFrame.pack(fill='both', expand='yes')

top = Message(userFrame, textvariable=userText, bg='light blue', fg='dark blue')
top.config(font=("Tahoma", 25, 'bold'))
top.pack(side='top', fill='both', expand='yes')

btn1 = Button(root, text='Run', font=('Tahoma', 18, 'bold'), bg='light green', fg='Green')
btn1.pack(fill='x', expand='no')

btn2 = Button(root, text='Close', font=('Tahoma', 18, 'bold'), bg='light yellow', fg='orange', command=root.destroy)
btn2.pack(fill='x', expand='no')

root.mainloop()