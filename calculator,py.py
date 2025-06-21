from tkinter import *

# Function to update expression in entry box
def press(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(num))

# Function to evaluate the expression
def equalpress():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Function to clear the entry
def clear():
    entry.delete(0, END)

# Create GUI window
root = Tk()
root.title("GUI Calculator")
root.geometry("300x400")

# Entry box
entry = Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=equalpress).grid(row=row, column=col)
    elif text == 'C':
        Button(root, text=text, padx=92, pady=20, font=("Arial", 14), command=clear).grid(row=row, column=col, columnspan=3)
    else:
        Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: press(t)).grid(row=row, column=col)

root.mainloop()
