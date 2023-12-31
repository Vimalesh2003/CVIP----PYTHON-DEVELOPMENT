import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields
entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

# Create operation dropdown
operations = ["+", "-", "*", "/"]
operation_var = tk.StringVar(root)
operation_var.set(operations[0])
operation_dropdown = tk.OptionMenu(root, operation_var, *operations)
operation_dropdown.pack()

# Create button to calculate
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Create label for displaying result
result_label = tk.Label(root)
result_label.pack()

root.mainloop()
