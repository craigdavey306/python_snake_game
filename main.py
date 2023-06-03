from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard
from constants import BOARD_WIDTH, BOARD_HEIGHT, X_MAX, X_MIN, Y_MIN, Y_MAX

screen = Screen()
screen.setup(width=BOARD_WIDTH, height=BOARD_HEIGHT)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Up, Down, Left, Right Arrow key bindings
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

# Main loop for the game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    head = snake.get_head()

    # Detect collision with food
    if head.distance(food) < food.size():
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with the walls
    if head.xcor() > X_MAX or head.xcor() < X_MIN or head.ycor() > Y_MAX or head.ycor() < Y_MIN:
        game_is_on = False
        scoreboard.game_over()

    # Detect snake collision with tail
    if snake.tail_collision():
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
