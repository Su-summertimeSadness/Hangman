from tkinter import *
import sqlite3

root = Tk()
root.title("Using databases")

# cur.execute("""CREATE TABLE addresses(
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer)
#
#         """)
# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
last_name = Entry(root, width=30)
last_name.grid(row=1, column=1, padx=20)
address_name = Entry(root, width=30)
address_name.grid(row=2, column=1, padx=20)
city_name = Entry(root, width=30)
city_name.grid(row=3, column=1, padx=20)
state_name = Entry(root, width=30)
state_name.grid(row=4, column=1, padx=20)
zip_name = Entry(root, width=30)
zip_name.grid(row=5, column=1, padx=20)

# Create Text box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
last_name_label = Label(root, text="Last Name")
last_name_label.grid(row=1, column=0)
address_name_label = Label(root, text="Address")
address_name_label.grid(row=2, column=0)
city_name_label = Label(root, text="City")
city_name_label.grid(row=3, column=0)
state_name_label = Label(root, text="State")
state_name_label.grid(row=4, column=0)
zip_name_label = Label(root, text="Zip code")
zip_name_label.grid(row=5, column=0)


# create submit button
def submit():
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()

    # Insert into database
    cur.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)",
                {
                    'first_name': f_name.get(),
                    'last_name': last_name.get(),
                    'address': address_name.get(),
                    'city': city_name.get(),
                    'state': state_name.get(),
                    'zipcode': zip_name.get()
                })

    conn.commit()
    conn.close()

    # clear text boxes
    f_name.delete(0, END)
    last_name.delete(0, END)
    address_name.delete(0, END)
    city_name.delete(0, END)
    state_name.delete(0, END)
    zip_name.delete(0, END)


submit_butt = Button(root, text="Add a record to DataBase", command=submit)
submit_butt.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# create query button
def query():
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()
    cur.execute("SELECT *, oid FROM addresses")
    records = cur.fetchall()
    # print(records)
    print_records = ''

    # Loop Thru Results
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + '\n'
    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()


query_button = Button(root, text="Show records", command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=132)

root.mainloop()
