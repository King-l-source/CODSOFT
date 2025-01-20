import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def create_table():
    conn = sqlite3.connect("todo_list.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            completed INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_task_to_db(title, description, due_date):
    conn = sqlite3.connect("todo_list.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)",
        (title, description, due_date),
    )
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect("todo_list.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task_in_db(task_id, title=None, description=None, due_date=None, completed=None):
    conn = sqlite3.connect("todo_list.db")
    cursor = conn.cursor()
    if title:
        cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (title, task_id))
    if description:
        cursor.execute("UPDATE tasks SET description = ? WHERE id = ?", (description, task_id))
    if due_date:
        cursor.execute("UPDATE tasks SET due_date = ? WHERE id = ?", (due_date, task_id))
    if completed is not None:
        cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (completed, task_id))
    conn.commit()
    conn.close()

def delete_task_from_db(task_id):
    conn = sqlite3.connect("todo_list.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def refresh_tasks(tree):
    for row in tree.get_children():
        tree.delete(row)
    tasks = get_tasks()
    for task in tasks:
        status = "Completed" if task[4] else "Pending"
        tree.insert("", "end", values=(task[0], task[1], task[2], task[3], status))

def add_task():
    title = title_entry.get()
    description = description_entry.get()
    due_date = due_date_entry.get()

    if not title:
        messagebox.showerror("Error", "Task title is required!")
        return

    add_task_to_db(title, description, due_date)
    refresh_tasks(task_tree)
    title_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Task added successfully!")

def delete_task():
    selected_item = task_tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "No task selected!")
        return

    task_id = task_tree.item(selected_item, "values")[0]
    delete_task_from_db(task_id)
    refresh_tasks(task_tree)
    messagebox.showinfo("Success", "Task deleted successfully!")

def mark_as_completed():
    selected_item = task_tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "No task selected!")
        return

    task_id = task_tree.item(selected_item, "values")[0]
    update_task_in_db(task_id, completed=1)
    refresh_tasks(task_tree)
    messagebox.showinfo("Success", "Task marked as completed!")

def mark_as_pending():
    selected_item = task_tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "No task selected!")
        return

    task_id = task_tree.item(selected_item, "values")[0]
    update_task_in_db(task_id, completed=0)
    refresh_tasks(task_tree)
    messagebox.showinfo("Success", "Task marked as pending!")

create_table()

root = tk.Tk()
root.title("To-Do List Application")

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Title").grid(row=0, column=0, padx=5, pady=5)
title_entry = tk.Entry(input_frame, width=30)
title_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Description").grid(row=1, column=0, padx=5, pady=5)
description_entry = tk.Entry(input_frame, width=30)
description_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Due Date (YYYY-MM-DD)").grid(row=2, column=0, padx=5, pady=5)
due_date_entry = tk.Entry(input_frame, width=30)
due_date_entry.grid(row=2, column=1, padx=5, pady=5)

add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

task_frame = tk.Frame(root)
task_frame.pack(pady=10)

columns = ("ID", "Title", "Description", "Due Date", "Status")
task_tree = ttk.Treeview(task_frame, columns=columns, show="headings")
for col in columns:
    task_tree.heading(col, text=col)
    task_tree.column(col, width=100)
task_tree.pack()

action_frame = tk.Frame(root)
action_frame.pack(pady=10)

delete_button = tk.Button(action_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=0, padx=10)

complete_button = tk.Button(action_frame, text="Mark as Completed", command=mark_as_completed)
complete_button.grid(row=0, column=1, padx=10)

pending_button = tk.Button(action_frame, text="Mark as Pending", command=mark_as_pending)
pending_button.grid(row=0, column=2, padx=10)

refresh_tasks(task_tree)

root.mainloop()

