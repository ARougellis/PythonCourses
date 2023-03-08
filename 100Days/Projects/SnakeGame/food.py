from turtle import Turtle
import random


# Step 4: Create food for snake
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh_loc()

    def refresh_loc(self):
        rand_x_coord = random.randint(-280, 280)
        rand_y_coord = random.randint(-280, 280)
        self.goto(x=rand_x_coord, y=rand_y_coord)
