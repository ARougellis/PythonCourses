import tkinter

window = tkinter.Tk()
window.title("Title Placeholder")
window.minsize(width=600, height=400)

# Label
label = tkinter.Label(text="This is a test label", font=("Ariel", 18, "italic"))
label.pack()


window.mainloop()