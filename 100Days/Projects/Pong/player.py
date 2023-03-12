from turtle import Turtle


class Player(Turtle):

    def __init__(self, starting_position):
        super(Player, self).__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(x=starting_position[0], y=0)

    def move_up(self):
        new_y_cor = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y_cor)

    def move_down(self):
        new_y_cor = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y_cor)




