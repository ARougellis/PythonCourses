import turtle
import pandas as pd

# Paths to data and image
image_path = './blank_states_img.gif'
states_path = './50_states.csv'

# Create Screen
screen = turtle.Screen()
screen.title("U.S. States Quiz")

screen.addshape(image_path)
turtle.shape(image_path)

# Read the States file into a df
states_df = pd.read_csv(states_path)
states_list = states_df.state.tolist()

guessed_states = []
while len(guessed_states) < 50:
    # create Input screen
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                   prompt="What is another state?").title()

    if user_answer == "Exit":
        # remaining_states_list = list(set(guessed_states).difference(states_list))
        # remaining_states_df = pd.DataFrame(remaining_states_list)
        remaining_states_list = []
        for state in states_list:
            if state not in guessed_states:
                remaining_states_list.append(state)
        remaining_states_df = pd.DataFrame(remaining_states_list)
        remaining_states_df.to_csv("./remaining_states.csv")
        break

    if user_answer in states_list:
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        state_row = states_df[states_df.state == user_answer]
        writer.goto(x=int(state_row.x), y=int(state_row.y))
        writer.write(state_row.state.item())

        guessed_states.append(state_row.state.item())
