import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating the player
player = Player()
# Creating the scoreboard
scoreboard = Scoreboard()
# Creating the cars
car_manager = CarManager()

# Controlling the Players
screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Player Levels Up
    if player.ycor() == 280:
        player.reset_position()
        scoreboard.level_up()
        car_manager.level_up()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
