import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 1:
            raise ValueError("Password length must be at least 1.")

        # Combine all possible characters
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate the password
        global generated_password
        generated_password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Generated Password: {generated_password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric length (at least 1).")

def copy_to_clipboard():
    if generated_password:
        root.clipboard_clear()
        root.clipboard_append(generated_password)
        root.update()  # Ensure the clipboard content is updated
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy. Please generate one first.")

root = tk.Tk()
root.title("Password Generator")

generated_password = ""

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Enter password length:").grid(row=0, column=0, padx=5, pady=5)
entry_length = tk.Entry(frame_input, width=10)
entry_length.grid(row=0, column=1, padx=5, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="Generated Password: ", font=("Arial", 12))
result_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

root.mainloop()

