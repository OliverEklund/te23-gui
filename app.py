from tkinter import *
from random import randint

dice_sides = 6

history=[]

def show(): 
    button.config( text = 'clicked.get()' ) 

def update_dice_sides(*args):
    global dice_sides
    dice_sides = int(clicked.get())

def roll():
    roll=randint(1,dice_sides)
    text_box_1.config(text=roll)
    history.append(roll)
    print(history)
    text_box.config(text=history)

options = [ 
    2,
    4,
    6,
    8,
    12,
    20,
    100
]

def submit():
    user_input = input_field.get()
    print(user_input) 

def BOMB():
    root.config(bg="red")
    root.after(2000, root.destroy) 

root = Tk()
root.title("Cool tärning")

clicked = StringVar()
clicked.set(options[0]) 
clicked.trace("w", update_dice_sides) 

text_box_1 = Label(root, text = 0)
text_box_1.pack()

roll_button = Button(root, text='Slå tärning', width=25, command=roll)
roll_button.pack()

nuke_button = Button(root, text='Bomb', width=25, command=BOMB)
nuke_button.pack()

drop = OptionMenu( root , clicked , *options )

button = Button(root, text="Submit", width=25, command=submit)
button.pack

input_field = Entry(root, width=30)
input_field.pack()

text_box = Label(root, text=0)
text_box.pack()

drop.pack()
root.mainloop()