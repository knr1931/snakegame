from turtle import Turtle
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        x_cor = random.randint(-(SCREEN_WIDTH//2 - 20), (SCREEN_WIDTH//2 - 20))
        y_cor = random.randint(-(SCREEN_HEIGHT//2 - 20), (SCREEN_HEIGHT//2 - 20))
        self.goto(x=x_cor, y=y_cor)
