from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}

greek_words_df = pd.read_csv('data/greek_words.csv')
greek_dict = greek_words_df.to_dict(orient="records")


def random_word_selector():
    global random_word
    random_word = random.choice(greek_dict)
    random_greek_word = random_word['Greek']

    canvas.itemconfig(greek_reminder, text="")
    canvas.itemconfig(card_language, text="Greek", fill="black")
    canvas.itemconfig(card_word, text=random_greek_word, fill="black")
    canvas.itemconfig(canvas_image, image=front_card_image)


def flip_card():
    random_english_word = random_word['English']

    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_english_word, fill="white")
    canvas.itemconfig(canvas_image, image=back_card_image)

    canvas.itemconfig(greek_reminder, text=random_word['Greek'], font=("Ariel", 20,))


# ---------------------------- UI SETUP ------------------------------- #

# WINDOW
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# IMAGES
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# CANVAS
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=front_card_image)
card_language = canvas.create_text(400, 150,
                                   text="",
                                   font=("Ariel", 40, "italic"),
                                   fill="black")
card_word = canvas.create_text(400, 263,
                               text="",
                               font=("Ariel", 60, "bold"),
                               fill="black")
greek_reminder = canvas.create_text(650, 75,
                                    text="",
                                    font=("Ariel", 20, "italic"),
                                    fill="white")
canvas.grid(column=0, row=0, columnspan=3)

# BUTTONS
#
unknown_button = Button(image=wrong_image,
                        highlightthickness=0,
                        command=random_word_selector)
unknown_button.grid(column=0, row=1)
#
known_button = Button(image=right_image,
                      highlightthickness=0,
                      command=random_word_selector)
known_button.grid(column=2, row=1)
#
flip_button = Button(text="Flip Card",
                     highlightbackground=BACKGROUND_COLOR,
                     command=flip_card)
flip_button.grid(column=1, row=1)

random_word_selector()

window.mainloop()
