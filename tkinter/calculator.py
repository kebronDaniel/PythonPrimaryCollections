from tkinter import *


windows = Tk()
windows.title("Mile to KM Converter")
windows.minsize(height=100, width=200)
windows.config(padx=10, pady=10)

entry = Entry(width=8)
entry.grid(column=1,row=0)
entry.insert(END,string=0)

equal_to = Label(text="is equal to")
equal_to.grid(column=0, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)


km_value = Label(text=0)
km_value.grid(column=1, row=1)


km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def convert():
    mile_value = int(entry.get())
    km = round(mile_value * 1.6)
    km_value.config(text=km)


calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1,row=2)








windows.mainloop()