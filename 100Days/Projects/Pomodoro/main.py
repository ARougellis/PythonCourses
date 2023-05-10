from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")

    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_seconds)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_seconds)
        timer_label.config(text="Work!")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    minute_count = math.floor(count / 60)
    second_count = count % 60
    if minute_count < 10:
        minute_count = f"0{minute_count}"
    if second_count < 10:
        second_count = f"0{second_count}"

    canvas.itemconfig(timer_text, text=f"{minute_count}:{second_count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# The Window
window = Tk()
window.title("Pomodoro")
# window.minsize(width=500, height=400)
window.config(padx=100, pady=100, bg=YELLOW)

# Setting the Background image
canvas = Canvas(width=200, height=250, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 125, image=tomato_image)
timer_text = canvas.create_text(100, 150, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# LABEL
timer_label = Label(
    text="Timer",
    font=(FONT_NAME, 50),
    bg=YELLOW,
    fg=GREEN
)
timer_label.grid(column=1, row=0)
#
check_label = Label(
    # font=(FONT_NAME, 50),
    bg=YELLOW,
    fg=GREEN
)
check_label.grid(column=1, row=3)

# BUTTON
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)
#
reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()
