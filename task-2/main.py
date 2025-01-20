import tkinter as tk
from tkinter import messagebox

def perform_calculation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Please select a valid operation.")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

root = tk.Tk()
root.title("Simple Calculator")

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Enter first number:").grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(frame_inputs, width=15)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Enter second number:").grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(frame_inputs, width=15)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

frame_operation = tk.Frame(root)
frame_operation.pack(pady=10)

operation_var = tk.StringVar(value="Select Operation")
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_menu = tk.OptionMenu(frame_operation, operation_var, *operations)
operation_menu.pack()

calculate_button = tk.Button(root, text="Calculate", command=perform_calculation)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()

