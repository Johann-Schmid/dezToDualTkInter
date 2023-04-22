import tkinter as tk
from tkinter import ttk

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        binary = str(remainder) + binary
    return binary

def decimal_to_hex(decimal):
    hex_digits = "0123456789abcdef"
    hex_num = ""
    while decimal > 0:
        remainder = decimal % 16
        decimal = decimal // 16
        hex_num = hex_digits[remainder] + hex_num
    return hex_num

def convert(decimal_entry, binary_var, hex_var):
    decimal = int(decimal_entry.get())
    binary = decimal_to_binary(decimal)
    hex_num = decimal_to_hex(decimal)
    binary_var.set(binary)
    hex_var.set(hex_num)

def main():
    app = tk.Tk()
    app.title("Decimal to Binary and Hex Converter")

    frame = ttk.Frame(app, padding="50")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    decimal_label = ttk.Label(frame, text="Decimal:")
    decimal_label.grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)

    decimal_var = tk.StringVar()
    decimal_entry = ttk.Entry(frame, textvariable=decimal_var)
    decimal_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

    binary_label = ttk.Label(frame, text="Binary:")
    binary_label.grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)

    binary_var = tk.StringVar()
    binary_entry = ttk.Entry(frame, textvariable=binary_var, state="readonly")
    binary_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

    hex_label = ttk.Label(frame, text="Hex:")
    hex_label.grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)

    hex_var = tk.StringVar()
    hex_entry = ttk.Entry(frame, textvariable=hex_var, state="readonly")
    hex_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

    convert_button = ttk.Button(frame, text="Convert", command=lambda: convert(decimal_entry, binary_var, hex_var))
    convert_button.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

    frame.columnconfigure(1, weight=1)

    app.mainloop()

if __name__ == "__main__":
    main()

