from turtle import Turtle
from snake import Snake


class Scoreboard():
    def __init__(self):
        self.score = 0
        self.score_board = Turtle()
        self.score_board.hideturtle()
        self.score_board.penup()
        self.score_board.color("white")
        self.score_board.goto(0, 260)  # Adjust as needed for your screen size
        self.update_score(self.score)  # Use the method to initialize the score display

    def update_score(self, score):
        self.score = score
        self.score_board.clear()  # Clear the previous score
        self.score_board.write(f"SCORE: {self.score}", align="center", font=("Arial", 16, "normal"))

    def increment_score(self):
        self.score += 1
        self.update_score(self.score)