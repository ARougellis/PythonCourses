import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# STEP 1: Create the snake (using oop and classes)
snake = Snake()
# STEP 4: Create food for snake to eat
food = Food()
# STEP 6: Create scoreboard and keep track of scores
scoreboard = Scoreboard()

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

    # STEP 5: Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh_loc()
        snake.extend()
        scoreboard.increase_score()

    # STEP 7: Detect out of bounds
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Snake collides with tail
    for segment in snake.segments:
        if segment == snake.snake_head:
            pass
        elif snake.snake_head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()
