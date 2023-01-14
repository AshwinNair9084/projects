from tkinter import *

root = Tk()
root.title("Simple Calculator")
e = Entry(root, width= 35)
e.grid(row=1, column=1,columnspan=4, pady=5, padx=5)
eval = ""

def input_number(x):
    temp = e.get() + str(x)
    e.delete(0, END)
    e.insert(0, temp)


def ac():
    global eval
    e.delete(0, END)
    eval = ""


def switch():
    temp = float(e.get()) * -1
    e.delete(0, END)
    if float(temp) == int(temp):
        e.insert(0, str(int(temp)))
    else:
        e.insert(0, str(float(temp)))


def percent():
    temp = float(e.get()) / 100
    e.delete(0, END)
    if float(temp) == int(temp):
        e.insert(0, str(int(temp)))
    else:
        e.insert(0, str(float(temp)))


def divide():
    global eval
    eval = eval +  e.get() + '/'
    e.delete(0, END)

def add():
    global eval
    eval = eval +  e.get() + '+'
    e.delete(0, END)

def multiply():
    global eval
    eval = eval +  e.get() + 'x'
    e.delete(0, END)

def subtract():
    global eval
    eval = eval +  e.get() + '-'
    e.delete(0, END)
    


def evaluate():
    global eval
    eval = eval + e.get()

    e.delete(0, END)
    temp = 0
    if '+' in eval:
        temp = float(eval.split('+')[0]) + float(eval.split('+')[1])
        eval = ""
    elif '-' in eval:
        temp = float(eval.split('-')[0]) - float(eval.split('-')[1])
        eval = ""
    elif  'x'  in eval:
        temp = float(eval.split('x')[0]) * float(eval.split('x')[1])
        eval = ""
    elif  '/' in eval:
        temp = float(eval.split('/')[0]) / float(eval.split('/')[1])
        eval = ""
    if float(temp) == int(temp):             
        e.insert(0, str(int(temp)))
    else:                                    
        e.insert(0, str(float(temp)))



        
# row 1 of numbers
Button(root, command=lambda: input_number(7), text="7", padx=15, pady=15).grid(row=3, column=1)
Button(root, command=lambda: input_number(8), text="8", padx=15, pady=15).grid(row=3, column=2)
Button(root, command=lambda: input_number(9), text="9", padx=15, pady=15).grid(row=3, column=3)

# row 2 of numbers
Button(root, command=lambda: input_number(4), text="4", padx=15, pady=15).grid(row=4, column=1)
Button(root, command=lambda: input_number(5), text="5", padx=15, pady=15).grid(row=4, column=2)
Button(root, command=lambda: input_number(6), text="6", padx=15, pady=15).grid(row=4, column=3)

# row 3 of numbers
Button(root, command=lambda: input_number(1), text="1", padx=15, pady=15).grid(row=5, column=1)
Button(root, command=lambda: input_number(2), text="2", padx=15, pady=15).grid(row=5, column=2)
Button(root, command=lambda: input_number(3), text="3", padx=15, pady=15).grid(row=5, column=3)

# row 1 of operations
Button(root, command=ac, text="AC", padx=15, pady=15).grid(row=2, column=1)
Button(root, command=switch, text="+/-", padx=15, pady=15).grid(row=2, column=2)
Button(root, command=percent, text="%", padx=15, pady=15).grid(row=2, column=3)
Button(root, command=divide, text="/", padx=15, pady=15).grid(row=2, column=4)

# row 2 of operations
Button(root, command=multiply, text="x", padx=15, pady=15).grid(row=3, column=4)

# row 3 of operations
Button(root, command=subtract, text="-", padx=15, pady=15).grid(row=4, column=4)

# row 4 of operations
Button(root, command=add, text="+", padx=15, pady=15).grid(row=5, column=4)

# row 5 of operations
Button(root, command=ac, text="0",width= 10  ,padx=15, pady=15).grid(row=6, column=1, columnspan=2)
Button(root, command=lambda: input_number("."), text=".", padx=15, pady=15).grid(row=6, column=3)
Button(root, command=evaluate, text="=", padx=15, pady=15).grid(row=6, column=4)

photo = PhotoImage(file = "calculator-icon.png")
root.iconphoto(False, photo)

root.mainloop()
