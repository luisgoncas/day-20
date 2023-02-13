from turtle import Turtle
from random import randint

LEFT_LIMIT = -280
RIGHT_LIMIT = 280


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = randint(LEFT_LIMIT, RIGHT_LIMIT)
        random_y = randint(LEFT_LIMIT, RIGHT_LIMIT)
        self.goto(random_x, random_y)