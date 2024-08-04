from turtle import Turtle
from constants import SCORE_BOARD_Y_COR, SCOREBOARD_CENTER_ALIGN, SCOREBOARD_FONT


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(SCORE_BOARD_Y_COR)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align=SCOREBOARD_CENTER_ALIGN, font=SCOREBOARD_FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over", move=False, align=SCOREBOARD_CENTER_ALIGN, font=SCOREBOARD_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
