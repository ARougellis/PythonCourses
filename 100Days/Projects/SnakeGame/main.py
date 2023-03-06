import time
from snake import Snake
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# STEP 1: Create the snake (using oop and classes)
snake = Snake()

# STEP 3: Control the snake (listening to key commands)
screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # STEP 2: Move the snake (using oop)
    snake.move()




screen.exitonclick()
