from tkinter import *
from random import randint

dice_sides = 6
high_score = 0

def show(): 
    button.config( text = 'clicked.get()' ) 

def update_dice_sides(*args):
    global dice_sides
    dice_sides = int(clicked.get())

def roll():
    roll=randint(1,dice_sides)
    text_box_1.config(text=roll)

options = [ 
    2,
    4,
    6,
    8,
    12,
    20,
    100
] 

root = Tk()
root.title("Cool tärning")

clicked = StringVar()
clicked.set(options[0]) 
clicked.trace("w", update_dice_sides) 

text_box_1 = Label(root, text = 0)
text_box_1.pack()

roll_button = Button(root, text='Slå tärning', width=25, command=roll)
roll_button.pack()

nuke_button = Button(root, text='Bomb', width=25, command=root.destroy)
nuke_button.pack()

drop = OptionMenu( root , clicked , *options )

text_box_2 = Label(root, text = high_score )
text_box_2.pack()

drop.pack() 
root.mainloop()