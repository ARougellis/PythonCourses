from tkinter import *


def button_clicked():
    print("Clicked")
    new_text = input.get()
    label.config(text=new_text)

# WINDOW
window = Tk()
window.title("Title Placeholder")
window.minsize(width=600, height=400)

# LABEL
label = Label(text="This is a test label", font=("Ariel", 18, "italic"))
label.config(text="new_text")
label.pack()

# BUTTON
button = Button(text="Click Me", command=button_clicked)
button.pack()

# ENTRY
input = Entry(width=10)
print(input.get())
input.pack()




window.mainloop()
