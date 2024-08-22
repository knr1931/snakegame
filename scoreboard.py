from turtle import Turtle
from constants import SCORE_BOARD_Y_COR, SCOREBOARD_CENTER_ALIGN, SCOREBOARD_FONT, HIGH_SCORE_DATA_FILENAME


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(HIGH_SCORE_DATA_FILENAME) as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(SCORE_BOARD_Y_COR)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=SCOREBOARD_CENTER_ALIGN, font=SCOREBOARD_FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(HIGH_SCORE_DATA_FILENAME, mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over", move=False, align=SCOREBOARD_CENTER_ALIGN, font=SCOREBOARD_FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
