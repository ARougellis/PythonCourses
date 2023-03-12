from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3

    def move(self):
        new_x_cor = self.xcor() + self.x_move
        new_y_cor = self.ycor() + self.y_move
        self.goto(x=new_x_cor, y=new_y_cor)

    def wall_bounce(self):
        self.y_move *= -1

    def player_bounce(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.player_bounce()
