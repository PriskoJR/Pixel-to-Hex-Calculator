import tkinter as tk
from tkinter import messagebox

def custom_calculator(input_number):
    multiplied = input_number * 0.111
    integer_part = int(multiplied)
    decimal_part = multiplied - integer_part
    multiplied_decimal = decimal_part * 255
    rounded_multiplied_decimal = int(multiplied_decimal)
    
    hex_integer_part = hex(integer_part)[2:].upper()
    hex_multiplied_decimal = hex(rounded_multiplied_decimal)[2:].upper()
    
    return hex_integer_part, hex_multiplied_decimal

def calculate_and_display(event=None):
    try:
        input_number = float(entry.get())
        hex_integer_part, hex_multiplied_decimal = custom_calculator(input_number)
        result = f"{hex_integer_part} {hex_multiplied_decimal}"
        result_label.config(text=result)
    except ValueError:
        messagebox.showerror("Error", "Input bukan angka yang valid. Coba lagi.")

def copy_to_clipboard():
    result = result_label.cget("text")
    if result:
        root.clipboard_clear()
        root.clipboard_append(result)


root = tk.Tk()
root.title("Hexadecimal Calculator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_label = tk.Label(frame, text="ENTER PIXEL NUMBER :")
entry_label.grid(row=0, column=0, pady=5)

entry = tk.Entry(frame)
entry.grid(row=0, column=1, pady=5)

# Bind the "Enter" key to the calculate_and_display function
entry.bind("<Return>", calculate_and_display)

calculate_button = tk.Button(frame, text="Calculate", command=calculate_and_display)
calculate_button.grid(row=1, column=0, padx=5, pady=5)

copy_button = tk.Button(frame, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=1, column=1, padx=5, pady=5)

result_label = tk.Label(frame, text="", font=("Arial", 14))
result_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
