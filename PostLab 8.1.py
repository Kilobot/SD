import tkinter as tk


temp_c = None
temp_f = None


def convert():

    global temp_c
    global temp_f


    try:
        val = temp_c.get()
        temp_f.set((val - 32) * 5/9)
    except:
        pass

def convert1():
    try:
        val = temp_f.get()
        temp_c.set((val / (5/9))+32)
    except:
        pass

root = tk.Tk()
root.title("Temperature Converter")


frame = tk.Frame(root)


frame.pack(fill=tk.BOTH, expand=True)


frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)

temp_c = tk.DoubleVar()
temp_f = tk.DoubleVar()

entry_celsius = tk.Entry(frame, width=7, textvariable=temp_c)
label_unitc = tk.Label(frame, text="Fahrenhiet")
label_equal = tk.Label(frame, text="")
entry_f = tk.Entry(frame, width=7, textvariable=temp_f)
label_fahrenheit = tk.Label(frame, textvariable=temp_f)
label_unitf = tk.Label(frame, text="Celcius")


button_convert1 = tk.Button(frame, text=">>>>", command=convert)
button_convert = tk.Button(frame, text="<<<<", command=convert1)

entry_celsius.grid(row=0, column=1, padx=5, pady=5)
entry_f.grid(row=0, column=0, padx=5, pady=5)
entry_f.grid(row=1, column=1, padx=5, pady=5)
label_unitc.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

label_unitf.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
button_convert.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky=tk.E)
button_convert1.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=tk.E)

entry_celsius.focus()
entry_f.focus()

root.mainloop()
