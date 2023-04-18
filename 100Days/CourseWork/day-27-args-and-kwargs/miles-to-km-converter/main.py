from tkinter import *


def convert():
    miles = mi_input.get()
    convert_to_km = round(int(miles)*1.609344, 1)
    calculated_km.config(text=convert_to_km)


# WINDOW
window = Tk()
window.title("Mile to km converter")
window.minsize(width=250, height=200)
window.config(padx=50, pady=50)

# ENTRY
mi_input = Entry(width=10)
mi_input.grid(column=1, row=0)

# BUTTON
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

# LABELS
#
# "Miles" label
mi_label = Label(text="Miles")
mi_label.grid(column=2, row=0)

# Calculated km value
calculated_km = Label(text="0")
calculated_km.grid(column=1, row=1)

# "is equal to" label
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# "km" label
km_label = Label(text="km")
km_label.grid(column=2, row=1)






window.mainloop()
