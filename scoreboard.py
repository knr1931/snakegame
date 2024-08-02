from turtle import Turtle
from constants import SCREEN_HEIGHT, SCOREBOARD_CENTER_ALIGN, SCOREBOARD_FONT


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(0.45 * SCREEN_HEIGHT)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align=SCOREBOARD_CENTER_ALIGN, font=SCOREBOARD_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
