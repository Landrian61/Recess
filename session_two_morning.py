import tkinter as tk


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))


def button_clear():
    entry.delete(0, tk.END)


def button_equals():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)


window = tk.Tk()
window.title("Simple Calculator")

calculator_title = tk.Label(window, text="Calculator", font=("Arial", 24))
calculator_title.grid(row=0, columnspan=3)

entry = tk.Entry(window, width=20, font=("Arial", 16))
entry.grid(row=1, columnspan=3, pady=10)

button_1 = tk.Button(window, text="1", width=5,
                     command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", width=5,
                     command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", width=5,
                     command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", width=5,
                     command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", width=5,
                     command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", width=5,
                     command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", width=5,
                     command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", width=5,
                     command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", width=5,
                     command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", width=5,
                     command=lambda: button_click(0))

button_add = tk.Button(window, text="+", width=5,
                       command=lambda: button_click("+"))
button_subtract = tk.Button(
    window, text="-", width=5, command=lambda: button_click("-"))
button_multiply = tk.Button(
    window, text="*", width=5, command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", width=5,
                          command=lambda: button_click("/"))

button_clear = tk.Button(window, text="Clear", width=11, command=button_clear)
button_equals = tk.Button(window, text="=", width=11, command=button_equals)

# Positioning buttons on the grid
button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_0.grid(row=5, column=0)

button_add.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)
button_divide.grid(row=5, column=3)

button_clear.grid(row=5, column=1, columnspan=2)
button_equals.grid(row=6, column=0, columnspan=4)

window.mainloop()
