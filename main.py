from turtle import Screen
from snake import Snake
import time
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, FOOD_COLLIDING_DISTANCE,
    WALL_COLLIDING_XCOR, WALL_COLLIDING_YCOR
)
from food import Food
from scoreboard import ScoreBoard

is_race_on = False
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

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

    # Detect collision with food
    if snake.head.distance(food) < FOOD_COLLIDING_DISTANCE:
        food.refresh()
        score_board.increase_score()

    # Detect Collision with the wall
    if (snake.head.xcor() > WALL_COLLIDING_XCOR or snake.head.xcor() < -WALL_COLLIDING_XCOR or
            snake.head.ycor() > WALL_COLLIDING_YCOR or snake.head.ycor() < -WALL_COLLIDING_YCOR):
        is_game_over = True
        score_board.game_over()

screen.exitonclick()
