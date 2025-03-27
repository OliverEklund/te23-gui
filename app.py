from tkinter import *
from random import randint

dice_sides = 6

def show(): 
    button.config( text = 'clicked.get()' ) 

def roll():
    roll=randint(1,dice_sides)
    text_box_1.config(text=roll)


options = [ 
    'so cool'
] 


root = Tk()
root.title("Cool tärning")

clicked = StringVar() 

text_box_1 = Label(root, text = 0)
text_box_1.pack()

roll_button = Button(root, text='Slå tärning', width=25, command=roll)
roll_button.pack()

nuke_button = Button(root, text='Bomb', width=25, command=root.destroy)
nuke_button.pack()

drop = OptionMenu( root , clicked , *options ) 
drop.pack() 

root.mainloop()