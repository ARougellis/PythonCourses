import tkinter

window = tkinter.Tk()
window.title("Title Placeholder")
window.minsize(width=600, height=400)

# Label
label = tkinter.Label(text="This is a test label", font=("Ariel", 18, "italic"))
label.pack()


# Button

# Create an event to get the button to work
def button_clicked():
    new_text = inputs.get()
    label["text"] = new_text


button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

# Entry
inputs = tkinter.Entry(width=15)
inputs.pack()



window.mainloop()
