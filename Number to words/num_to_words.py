from tkinter import *
from num2words import num2words

root = Tk()
root.title("Number to words converter")
root.geometry("650x400")

# This is the output label
label = Label(root, text="", font=('arial', 15, 'bold'), fg="black")


def converter(temp=""):
    try:
        label.config(text="")
        label.place(x=50, y=300)
        label.config(text=num2words(input_bar.get()))

    except:

        label.config(text="")
        label.place(x=50, y=300)
        label.config(text="Invalid input please re-enter the correct input")


Label(root, text="Convert Your Number To Words ", font=('arial', 30, 'bold'), fg="blue").place(x=50, y=10)
Label(root, text="Accepted formats : ", font=('arial', 15, 'bold'), fg="green").place(x=50, y=80)
Label(root, text="+ve number", font=('arial', 15, 'bold'), fg="green").place(x=80, y=100)
Label(root, text="-ve number", font=('arial', 15, 'bold'), fg="green").place(x=80, y=120)
Label(root, text="decimal number", font=('arial', 15, 'bold'), fg="green").place(x=80, y=140)

Label(root, text="Enter the number to be converted :", font=('arial', 15, 'bold'), fg="blue").place(x=50, y=200)

input_bar = Entry(root, width=40)
input_bar.place(x=50, y=230)
input_bar.insert(0, "Enter here", )

Button(root, text="convert", command=converter).place(x=300, y=270)

# This binds the enter key to the input bar
input_bar.bind('<Return>', converter)

root.mainloop()
