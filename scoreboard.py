FONT = ("Courier", 20, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-230, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def update_level(self):
        self.clear()
        self.score += 1
        self.goto(-230, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
