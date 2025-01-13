

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    # Define a method to create the ball object
    def create_ball(self):
        self.dot(20, "white")
        self.goto(0, 0)
        self.penup()
        self.hideturtle()




