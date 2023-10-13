import tkinter
from tkinter import *
from PIL import ImageTk, Image
import mouse
####################################
#print(mouse.get_position())
####################################
root = Tk()
bg = ImageTk.PhotoImage(file="mask.png")
root.title("mask")
root.attributes('-alpha', 0.3)
canvas = Canvas(root, width=500, height=500)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor='nw')

def resize_bg(event):
    global bgg, resized, bg2
    # open image to resize it
    bgg = Image.open("mask.png")
    # resize the image with width and height of root
    resized = bgg.resize((event.width, event.height), Image.ANTIALIAS)
    bg2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=bg2, anchor='nw')

root.bind("<Configure>", resize_bg)
root.mainloop()


