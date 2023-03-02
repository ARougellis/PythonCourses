import random
from turtle import Turtle, Screen

screen = Screen()

# first, lets customize the screen a bit...
screen.setup(width=500, height=400)

is_race_on = False

# screen pop-up to get user input
user_input_prompt = "Which turtle will win the race? (blue, green, purple, red, brown) : "
user_bet = screen.textinput(title="Make your bet!", prompt=user_input_prompt)

colors = ["blue", "green", "purple", "red", "brown"]
y_coord = [0, -50, 50, -100, 100]
turtle_list = []

for index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.speed("fastest")
    new_turtle.penup()
    new_turtle.goto(x=-225, y=y_coord[index])
    turtle_list.append(new_turtle)


if user_bet:
    start_race = True

while start_race:
    for turtles in turtle_list:
        if turtles.xcor() > 230:
            winner = turtles.pencolor()
            if user_bet == winner:
                print(f"You and your {winner} turtle won!")
            else:
                print(f"You and your {user_bet} turtle lost...")
            start_race = False

        turtles.speed("normal")
        turtles.forward(random.randint(0, 10))


screen.exitonclick()
