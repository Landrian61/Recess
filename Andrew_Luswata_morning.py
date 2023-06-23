import tkinter as tk
from tkinter import font

# Button click event


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Clear button event


def button_clear():
    entry.delete(0, tk.END)

# Equals button event


def button_equals():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)


# Create the main window
window = tk.Tk()
window.title("Luswata Andrew's Simple Calculator")

# Define colors
bg_color = "#F0F0F0"
button_color = "#E0E0E0"
button_active_color = "#D0D0D0"
button_text_color = "#000000"

# Set the window background color
window.config(bg=bg_color)

# Set the font style
font_style = font.Font(family="Arial", size=16)

# Create the entry field
entry = tk.Entry(window, width=18, font=font_style, bd=5, relief=tk.SUNKEN)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Function to create rounded buttons


def create_rounded_button(text, row, col, col_span=1, bg=button_color):
    button = tk.Button(window, text=text, width=5, font=font_style, bg=bg,
                       activebackground=button_active_color, fg=button_text_color,
                       bd=0, relief=tk.RAISED, command=lambda: button_click(text))
    button.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5)
    return button


# Create calculator buttons
row = 1
col = 0
for button_text in buttons:
    if col == 4:
        col = 0
        row += 1

    if button_text == "=":
        col_span = 2
        bg = button_color
    else:
        col_span = 1
        bg = button_color

    create_rounded_button(button_text, row, col, col_span, bg)
    col += col_span

# Create the clear button
clear_button = create_rounded_button("C", row + 1, 0, 2, bg="#F08080")
clear_button.config(command=button_clear)

# Create the equals button
equals_button = create_rounded_button("=", row + 1, 2, 2, bg="#6495ED")
equals_button.config(command=button_equals)

window.mainloop()
