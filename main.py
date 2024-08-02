from turtle import Turtle, Screen
from snake import Snake
import time

screen_width = 800
screen_height = 600

is_race_on = False
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=screen_width, height=screen_height)
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

is_game_over = False

while not is_game_over:
    screen.update()
    time.sleep(.1)

    snake.move()

screen.exitonclick()
