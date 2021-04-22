import tkinter
import random
from PIL import Image,ImageTk

root = tkinter.Tk()
root.geometry("400x400")
root.title("Roll the dice")

bl = tkinter.Label(root,text="")
bl.pack()

heading = tkinter.Label(root,text="Roll the dice",fg="yellow",bg="dark green",font="Helvetica 16 bold italic")
heading.pack()

dice=["die1.png","die2.png","die3.png","die4.png","die5.png","die6.png"]
diceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

imageLabel = tkinter.Label(root,image=diceImage)
imageLabel.image = diceImage
imageLabel.pack(expand = True)

def roll_dice():
    diceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    imageLabel.configure(image=diceImage)
    imageLabel.image = diceImage
    
button = tkinter.Button(root,text = "Click to roll!",fg = "Red",command = roll_dice)
button.pack(expand = True)

root.mainloop()