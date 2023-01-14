from tkinter import *
import sqlite3

root = Tk()
root.title("Address Book")
root.geometry("400x600")

'''
# Databases

# This will create a new database or connect to an existing one
conn = sqlite3.connect('address_book.db')

# This will form a cursor to work with the database
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE addresses(
    first_name text,
    last_name text,
    phone_number integer,
    city text,
    zipcode text
    )""")

# commit your changes
conn.commit()

# close your connection
conn.close()
'''


def submit():
    # Databases

    # This will create a new database or connect to an existing one
    conn = sqlite3.connect('address_book.db')

    # This will form a cursor to work with the database
    c = conn.cursor()

    # Submitting the entries
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :phone, :city, :zipcode )",
              {
                  'f_name': First.get(),
                  'l_name': Last.get(),
                  'phone': Phone.get(),
                  'city': City.get(),
                  'zipcode': Zipcode.get(),

              }

              )

    # Commit your changes
    conn.commit()

    # close your connection
    conn.close()
    First.delete(0, END)
    Last.delete(0, END)
    Phone.delete(0, END)
    City.delete(0, END)
    Zipcode.delete(0, END)


def view():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    c.execute("SELECT *,oid FROM addresses")
    all_items = c.fetchall()

    data = ""
    for item in all_items:
        data += str(item) + "\n"

    Label(root, text=data, font=('arial', 12, 'italic'), fg="red").place(x=50, y=300)
    conn.commit()
    conn.close()


def delete():
    top = Toplevel()
    top.title('Delete a Entry')
    top.geometry("400x200")

    Label(top, text="Delete an Entry ", font=('arial', 30, 'bold'), fg="blue").place(x=30, y=10)
    Label(top, text="Enter the id :", font=('arial', 15), fg="black").place(x=50, y=60)
    id_entry = Entry(top)
    id_entry.place(x=170, y=60)

    def delete_oid():
        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()

        c.execute("DELETE from addresses WHERE oid =" + str(id_entry.get()))

        conn.commit()
        conn.close()
        id_entry.delete(0, END)

    Button(top, text="Delete form database", command=delete_oid).place(x=50, y=120)
    Button(top, text="Exit", command=top.destroy).place(x=300, y=120)

def edit():
    editor = Toplevel()
    editor.title('Delete a Entry')
    editor.geometry("400x400")

    def selectID():
        Firstedit.delete(0, END)
        Lastedit.delete(0, END)
        Phoneedit.delete(0, END)
        Cityedit.delete(0, END)
        Zipcodeedit.delete(0, END)

        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()

        c.execute("SELECT * FROM addresses WHERE oid = " + id_entry.get())
        all_items = c.fetchall()[0]

        Firstedit.insert(0, all_items[0])
        Lastedit.insert(0, all_items[1])
        Phoneedit.insert(0, all_items[2])
        Cityedit.insert(0, all_items[3])
        Zipcodeedit.insert(0, all_items[4])

        conn.commit()
        conn.close()

    Label(editor, text="Edit an Entry ", font=('arial', 30, 'bold'), fg="blue").place(x=30, y=10)
    Label(editor, text="Enter the id :", font=('arial', 15), fg="black").place(x=50, y=60)
    id_entry = Entry(editor)
    id_entry.place(x=170, y=60)
    Button(editor, text="Select the id", command=selectID).place(x=50, y=90)
    def edit_oid():
        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()

        c.execute("""UPDATE addresses SET
            first_name = :f,
            last_name = :l,
            phone_number = :ph,
            city = :c,
            zipcode = :z
            
            WHERE oid = :oid""",
        {
            'f':Firstedit.get(),
            'l':Lastedit.get(),
            'ph':Phoneedit.get(),
            'c':Cityedit.get(),
            'z':Zipcodeedit.get(),
            'oid':id_entry.get()

        })

        conn.commit()
        conn.close()
        id_entry.delete(0, END)
        Firstedit.delete(0, END)
        Lastedit.delete(0, END)
        Phoneedit.delete(0, END)
        Cityedit.delete(0, END)
        Zipcodeedit.delete(0, END)

    Label(editor, text="First Name :", font=('arial', 15), fg="black").place(x=50, y=140)
    Label(editor, text="Last Name :", font=('arial', 15), fg="black").place(x=50, y=170)
    Label(editor, text="Phone Number :", font=('arial', 15), fg="black").place(x=50, y=200)
    Label(editor, text="City :", font=('arial', 15), fg="black").place(x=50, y=230)
    Label(editor, text="Zipcode :", font=('arial', 15), fg="black").place(x=50, y=260)

    Firstedit = Entry(editor)
    Firstedit.place(x=170, y=140)
    Lastedit = Entry(editor)
    Lastedit.place(x=170, y=170)
    Phoneedit = Entry(editor)
    Phoneedit.place(x=170, y=200)
    Cityedit = Entry(editor)
    Cityedit.place(x=170, y=230)
    Zipcodeedit = Entry(editor)
    Zipcodeedit.place(x=170, y=260)

    Button(editor, text="Edit into database", command=edit_oid).place(x=50, y=310)
    Button(editor, text="Exit", command=editor.destroy).place(x=300, y=310)



# Building out the gui for the app
Label(root, text="Phone Book ", font=('arial', 30, 'bold'), fg="blue").place(x=30, y=10)
Label(root, text="First Name :", font=('arial', 15), fg="black").place(x=50, y=60)
Label(root, text="Last Name :", font=('arial', 15), fg="black").place(x=50, y=90)
Label(root, text="Phone Number :", font=('arial', 15), fg="black").place(x=50, y=120)
Label(root, text="City :", font=('arial', 15), fg="black").place(x=50, y=150)
Label(root, text="Zipcode :", font=('arial', 15), fg="black").place(x=50, y=180)

First = Entry(root)
First.place(x=170, y=60)
Last = Entry(root)
Last.place(x=170, y=90)
Phone = Entry(root)
Phone.place(x=170, y=120)
City = Entry(root)
City.place(x=170, y=150)
Zipcode = Entry(root)
Zipcode.place(x=170, y=180)

Button(root, text="Add new contact", command=submit).place(x=150, y=220)
Button(root, text="View database", command=view).place(x=20, y=250)
Button(root, text="Delete Entry", command=delete).place(x=160, y=250)
Button(root, text="Edit Entry", command=edit).place(x=280, y=250)
Button(root, text="Exit", command=root.quit).place(x=300, y=550)

root.mainloop()
