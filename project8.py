# Write a python code to build simple GUI calculator

import tkinter as tk

def evaluate_expression():
    try:
        result.set(eval(entry.get()))
    except Exception as e:
        result.set("Error")

# Create a Tkinter window
window = tk.Tk()
window.title("Simple Calculator")

# Entry widget to input expression
entry = tk.Entry(window, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

# Button widgets for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0
for button in buttons:
    tk.Button(window, text=button, font=('Arial', 14), command=lambda button=button: entry.insert(tk.END, button)).grid(row=row, column=col, sticky='nsew')
    col += 1
    if col > 3:
        col = 0
        row += 1

# Result display
result = tk.StringVar()
result.set("")
result_label = tk.Label(window, textvariable=result, font=('Arial', 14), anchor='e', padx=10)
result_label.grid(row=row, column=0, columnspan=4, sticky='nsew')

window.mainloop()
