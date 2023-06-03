from turtle import Turtle
from typing import List, Tuple

# Constants specific to the Snake object.
# Initial starting position for the snake body segments.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# Distance to move the snake each move.
MOVE_DISTANCE = 20
# Coordinates for moving the snake up, down, left, and right.
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self._segments: List[Turtle] = []
        self._create_snake_body()
        self._head = self._segments[0]

    def _create_snake_body(self) -> None:
        for position in STARTING_POSITIONS:
            self._add_segment(position)

    def _add_segment(self, position: Tuple[float, float]):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self._segments.append(new_segment)

    def extend(self):
        self._add_segment(self._segments[-1].position())

    def get_head(self) -> Turtle:
        return self._head

    def move(self) -> None:
        for segment_number in range(len(self._segments) - 1, 0, -1):
            prev = self._segments[segment_number - 1]
            new_x = prev.xcor()
            new_y = prev.ycor()
            self._segments[segment_number].goto(new_x, new_y)
        self._head.forward(MOVE_DISTANCE)

    def move_up(self) -> None:
        if self._head.heading() != DOWN:
            self._head.setheading(UP)

    def move_down(self) -> None:
        if self._head.heading() != UP:
            self._head.setheading(DOWN)

    def move_left(self) -> None:
        if self._head.heading() != RIGHT:
            self._head.setheading(LEFT)

    def move_right(self) -> None:
        if self._head.heading() != LEFT:
            self._head.setheading(RIGHT)

    def tail_collision(self) -> bool:
        collides = False

        for segment in self._segments[1:]:
            if self._head.distance(segment) < 10:
                collides = True
                break

        return collides
