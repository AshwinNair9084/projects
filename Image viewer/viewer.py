from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

root.title("Image Viewer")
photo = PhotoImage(file = "pic.png")
root.iconphoto(False, photo)

list_images = os.listdir("Images")
if '.DS_Store' in list_images:
    list_images.remove('.DS_Store')


imagecount = 0



def forward(x):
    global imagecount
    global img

    if x + 1 == len(list_images) - 1:
        forwardbutton.config(state=DISABLED)

    imagecount += 1
    if imagecount>0:
        backwardbutton.config(state=NORMAL)

    img = ImageTk.PhotoImage((Image.open("Images/" + list_images[imagecount])).resize((400, 400)))
    imagelabel = Label(image=img)
    imagelabel.grid(row=0, column=0, columnspan=3)
    status.config(text=f"Image {imagecount + 1} of {len(list_images)}")

def backward(x):
    global imagecount
    global img

    if x -1 == 0:
        backwardbutton.config(state=DISABLED)

    imagecount -= 1
    if imagecount< len(list_images) - 1:
        forwardbutton.config(state=NORMAL)

    img = ImageTk.PhotoImage((Image.open("Images/" + list_images[imagecount])).resize((400, 400)))
    imagelabel = Label(image=img)
    imagelabel.grid(row=0, column=0, columnspan=3)
    status.config(text=f"Image {imagecount + 1} of {len(list_images)}")


img = ImageTk.PhotoImage((Image.open("Images/"+list_images[imagecount])).resize((400, 400)))
imagelabel = Label(image= img)
imagelabel.grid(row=0,column= 0, columnspan=3)
Button(root, command = root.quit, text="Exit").grid(row=1, column=1)
forwardbutton = Button(root, command = lambda: forward(imagecount), text=">>")
forwardbutton.grid(row=1, column=2)
backwardbutton = Button(root,command = lambda: backward(imagecount), text="<<", state=DISABLED)
backwardbutton.grid(row=1, column=0,pady=10)
status = Label(root, text= f"Image {imagecount + 1} of {len(list_images)}", bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


root.mainloop()
