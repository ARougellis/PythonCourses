from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import random
# import time

# Create Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Creating scoreboard
scoreboard = Scoreboard()
# Creating the ball
ball = Ball()

# Creating the Players
l_player = Player((-350, 0))
r_player = Player((350, 0))

# Controlling the Players
screen.listen()
screen.onkeypress(l_player.move_up, "w")
screen.onkeypress(l_player.move_down, "s")
screen.onkeypress(r_player.move_up, "Up")
screen.onkeypress(r_player.move_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()

    ball.move()

    # Bouncing off top and bottom boundaries
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_bounce()

    # Bounce off left player
    if ball.distance(l_player) < 50 and ball.xcor() < -330:
        ball.player_bounce()

    # Bounce off right player
    if ball.distance(r_player) < 50 and ball.xcor() > 330:
        ball.player_bounce()

    # Left Player gets a POINT
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l_score()

    # Right Player gets a POINT
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r_score()



screen.exitonclick()
