import tkinter as tk
from tkinter import *
# import tkinter, graphic interface

# first step, create a user interface
# second step, add functionalities

root = tk.Tk() # create a window
root.geometry("600x600") # the dimensions of the window
root.configure(background="white") # the background color of the window
root.title("calculatrice") # the title

# if you do not want to resize the window, decomment this :
# root.resizable(width=False, height=False)

# by convention, the variable that stores the graphics window
# the name is either root or win

# create an input filed
entry = tk.Entry(root, width=20, font=("Serif", 20))
entry.grid(row=0, column=0, columnspan=5)
entry.configure(background="black")

# create buttons
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", ".", "=", "/"
]

expression = "" # initialized the global variable expression

row, col = 1, 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=("Serif", 16),
              command=lambda button=button: button_click(button)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# create a backspace button
tk.Button(root, text="←", padx=40, pady=10, font=("Serif", 16),
          command=lambda: button_click("←")).grid(row=5, column=5)

# create a clear button to clear the interface
tk.Button(root, text="clear", padx=40, pady=10, font=("Serif", 16),
          command=lambda: button_click("clear")).grid(row=6, column=5)

label = tk.Label(root, text="welcome on the python calculator", font=("Serif", 14), bg="black")
label.grid(row=row, columnspan=4, pady=10)

def button_click(item):
    global expression

    if item == "=":
        try:
            result = str(eval(expression))
            entry.delete(0, END)
            entry.insert(0, result)
            expression = result
        except:
            entry.delete(0, END)
            entry.insert(0, "error")
            expression = ""
    elif item == "clear":
        expression = ""
        entry.delete(0, END)
    elif item == "←":
        expression = expression[:-1]
        entry.delete(0, END)
        entry.insert(0, expression)
    else:
        expression += str(item)
        entry.delete(0, END)
        entry.insert(0, expression)


root.mainloop()
