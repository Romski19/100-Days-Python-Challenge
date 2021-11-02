from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", align="center", font=("Arial", 12, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        string_highest = str(self.high_score)
        with open("data.txt", mode="w") as new_score:
            new_score.write(string_highest)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
