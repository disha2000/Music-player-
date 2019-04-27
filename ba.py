import tkinter
from PIL import Image,ImageTk

# open a SPIDER image and convert to byte format    
im = Image.open('b.jpg')

root = tkinter.Tk()  # A root window for displaying objects

# Convert the Image object into a TkPhoto object
tkimage = ImageTk.PhotoImage(im)

tkinter.Label(root, image=tkimage, text="Update User", compound=tkinter.LEFT).pack() # Put it in the display window

root.mainloop() # 