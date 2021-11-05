from turtle import Turtle
import time
FONT = ("Arial", 24, "normal")


class Countdown(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(150, 260)
        self.start_time = 10 * 60
        self.min = 0
        self.sec = 0
        self.countdown_timer()

    def countdown_timer(self):
        for timer in range(self.start_time, -1 , -1):
            self.min = self.start_time // 60
            self.sec = self.start_time % 60
            self.write(f"Time %s" %timer, align="left", font=FONT)
            time.sleep(1)