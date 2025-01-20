import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

def initialize_database():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            address TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)", 
                   (name, phone, email, address))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Contact added successfully!")
    clear_entries()
    view_contacts()

def view_contacts():
    for row in contact_tree.get_children():
        contact_tree.delete(row)

    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone FROM contacts")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        contact_tree.insert("", "end", values=row)

def search_contact():
    query = search_entry.get()
    if not query:
        messagebox.showerror("Error", "Please enter a name or phone number to search!")
        return

    for row in contact_tree.get_children():
        contact_tree.delete(row)

    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone FROM contacts WHERE name LIKE ? OR phone LIKE ?", 
                   (f"%{query}%", f"%{query}%"))
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        contact_tree.insert("", "end", values=row)

def update_contact():
    selected_item = contact_tree.focus()
    if not selected_item:
        messagebox.showerror("Error", "Please select a contact to update!")
        return

    contact_id = contact_tree.item(selected_item)["values"][0]
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE contacts 
        SET name = ?, phone = ?, email = ?, address = ? 
        WHERE id = ?
    """, (name, phone, email, address, contact_id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Contact updated successfully!")
    clear_entries()
    view_contacts()

def delete_contact():
    selected_item = contact_tree.focus()
    if not selected_item:
        messagebox.showerror("Error", "Please select a contact to delete!")
        return

    contact_id = contact_tree.item(selected_item)["values"][0]

    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Contact deleted successfully!")
    view_contacts()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def populate_fields(event):
    selected_item = contact_tree.focus()
    if not selected_item:
        return

    contact_id, name, phone = contact_tree.item(selected_item)["values"]

    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
    contact = cursor.fetchone()
    conn.close()

    clear_entries()
    name_entry.insert(0, contact[1])
    phone_entry.insert(0, contact[2])
    email_entry.insert(0, contact[3])
    address_entry.insert(0, contact[4])

initialize_database()

root = tk.Tk()
root.title("Contact Book")
root.geometry("700x500")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Phone").grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(frame, width=30)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Email").grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Address").grid(row=3, column=0, padx=5, pady=5)
address_entry = tk.Entry(frame, width=30)
address_entry.grid(row=3, column=1, padx=5, pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", width=15, command=add_contact)
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(button_frame, text="Update Contact", width=15, command=update_contact)
update_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Contact", width=15, command=delete_contact)
delete_button.grid(row=0, column=2, padx=5)

clear_button = tk.Button(button_frame, text="Clear Fields", width=15, command=clear_entries)
clear_button.grid(row=0, column=3, padx=5)

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search").grid(row=0, column=0, padx=5, pady=5)
search_entry = tk.Entry(search_frame, width=40)
search_entry.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(search_frame, text="Search", width=15, command=search_contact)
search_button.grid(row=0, column=2, padx=5)

columns = ("ID", "Name", "Phone")
contact_tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
contact_tree.pack(pady=20)

contact_tree.heading("ID", text="ID")
contact_tree.heading("Name", text="Name")
contact_tree.heading("Phone", text="Phone")
contact_tree.column("ID", width=50)
contact_tree.column("Name", width=200)
contact_tree.column("Phone", width=150)

contact_tree.bind("<ButtonRelease-1>", populate_fields)
view_contacts()
root.mainloop()
