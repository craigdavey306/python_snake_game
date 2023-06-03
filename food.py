from turtle import Turtle
import random

from constants import X_MAX, X_MIN, Y_MAX, Y_MIN
from constants import DEFAULT_PIXEL_SIZE


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self) -> None:
        random_x = random.randint(X_MIN, X_MAX)
        random_y = random.randint(Y_MIN, Y_MAX)
        self.goto(random_x, random_y)

    def size(self) -> float:
        # turtlesize() returns a tuple where the last element is the size.
        size = self.turtlesize()[-1]
        return size * DEFAULT_PIXEL_SIZE
