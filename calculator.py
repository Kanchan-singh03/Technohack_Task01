import tkinter as tk

def on_click(btn_text):
    current_text = entry.get()
    if btn_text == '=':
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif btn_text == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, btn_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display input and output
entry = tk.Entry(root, width=20, font=('Arial', 16), justify='center')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Create buttons and assign the on_click function
row_val = 1
col_val = 0
for btn in buttons:
    tk.Button(root, text=btn, width=5, height=2,
              command=lambda b=btn: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the main event loop
root.mainloop()
