from turtle import Turtle

MOVE_DISTANCE = 20
UP_DIRECTION = 90
DOWN_DIRECTION = 270
LEFT_DIRECTION = 180
RIGHT_DIRECTION = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    # STEP 1: Create the snake
    def create_snake(self):
        x_pos = 0
        for i in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(x=x_pos, y=0)
            self.segments.append(snake)
            x_pos -= 20

    # STEP 2: Move the snake
    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x_pos = self.segments[segment - 1].xcor()
            new_y_pos = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x=new_x_pos, y=new_y_pos)

        self.segments[0].forward(MOVE_DISTANCE)

    def turn_up(self):
        if self.snake_head.heading() != DOWN_DIRECTION:
            self.snake_head.setheading(UP_DIRECTION)

    def turn_down(self):
        if self.snake_head.heading() != UP_DIRECTION:
            self.snake_head.setheading(DOWN_DIRECTION)

    def turn_left(self):
        if self.snake_head.heading() != RIGHT_DIRECTION:
            self.snake_head.setheading(LEFT_DIRECTION)

    def turn_right(self):
        if self.snake_head.heading() != LEFT_DIRECTION:
            self.snake_head.setheading(RIGHT_DIRECTION)
