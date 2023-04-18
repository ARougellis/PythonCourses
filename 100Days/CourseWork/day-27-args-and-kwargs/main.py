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
label = Label(text="This is a test label", font=("Ariel", 18, "bold"))
label.config(text="new_text")
# label.pack()
# label.place(x=0, y=0)
label.grid()


# BUTTON
button = Button(text="Click Me", command=button_clicked)
# button.pack()
# button.place(x=300, y=200)
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# ENTRY
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)




window.mainloop()
