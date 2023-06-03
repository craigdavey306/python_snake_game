from turtle import Turtle

# Constants specific to the scoreboard object
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self._score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self._update_scoreboard()

    def _update_scoreboard(self) -> None:
        self.write(f'Score: {self._score}', align=ALIGNMENT, font=FONT)

    def increase_score(self) -> None:
        self._score += 1
        self.clear()
        self._update_scoreboard()

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write('GAME OVER!', align=ALIGNMENT, font=FONT)
