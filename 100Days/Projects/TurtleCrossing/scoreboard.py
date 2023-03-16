from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.lvl = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-230, y=270)
        self.write(f"Level : {self.lvl}", align=SCOREBOARD_ALIGNMENT, font=FONT)

    def level_up(self):
        self.lvl += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=SCOREBOARD_ALIGNMENT, font=FONT)
