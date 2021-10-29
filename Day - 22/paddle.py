from turtle import Turtle

START_POS = 350, 0


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        up_y = self.ycor() + 20
        self.goto(self.xcor(), up_y)

    def down(self):
        down_y = self.ycor() - 20
        self.goto(self.xcor(), down_y)
