from tkinter import *
from random import randint

def roll():
    roll=randint(1,6)
    text_box.config(text=roll)

root = Tk()
root.title("Cool tärning")

text_box = Label(root, text = 0)
text_box.pack()

roll_button = Button(root, text='Slå tärning', width=25, command=roll)
roll_button.pack()

nuke_button = Button(root, text='Nuke the moon', width=25, command=root.)
nuke_button.pack()

button = Button(root, text='Quit', width=25, command=root.destroy)
button.pack()

root.mainloop()