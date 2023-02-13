from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def end_game(self):
        self.goto(0, 0)
        self.write("End Game!", align=ALIGNMENT, font=FONT)
