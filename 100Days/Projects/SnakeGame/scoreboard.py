from turtle import Turtle

SCOREBOARD_ALIGNMENT = "center"
SCOREBOARD_FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
