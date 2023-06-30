import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedStyle
from tkinter.ttk import Button, Entry, Style


class ReceiptPrinter:
    def __init__(self, master):
        self.master = master
        master.title("Receipt Printer")

        # Apply Material Design theme
        style = ThemedStyle(master)
        style.set_theme("arc")

        # Custom styles for widgets
        self.custom_style = Style()
        self.custom_style.configure("TEntry", padding=5)

        # Create labels and entry fields
        self.label_name = tk.Label(master, text="Name:")
        self.label_name.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        self.entry_name = Entry(master, style="TEntry")
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_items = tk.Label(master, text="Items (comma-separated):")
        self.label_items.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        self.entry_items = Entry(master, style="TEntry")
        self.entry_items.grid(row=1, column=1, padx=10, pady=10)

        self.label_total = tk.Label(master, text="Total:")
        self.label_total.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
        self.entry_total = Entry(master, style="TEntry")
        self.entry_total.grid(row=2, column=1, padx=10, pady=10)

        # Create print button
        self.print_button = Button(
            master, text="Print Receipt", command=self.print_receipt)
        self.print_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Center the window on the screen
        window_width = 400
        window_height = 250
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Disable resizing of the window
        master.resizable(False, False)

    def print_receipt(self):
        name = self.entry_name.get()
        items = self.entry_items.get()
        total = self.entry_total.get()

        if not name or not items or not total:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        receipt = f"Name: {name}\nItems: {items}\nTotal: {total}"
        messagebox.showinfo("Receipt", receipt)

        # Clear the entry fields
        self.entry_name.delete(0, tk.END)
        self.entry_items.delete(0, tk.END)
        self.entry_total.delete(0, tk.END)


# Create the main window
root = tk.Tk()

# Create an instance of the ReceiptPrinter class
receipt_printer = ReceiptPrinter(root)

# Start the GUI event loop
root.mainloop()
