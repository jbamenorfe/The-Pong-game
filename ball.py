

from turtle import Turtle
START_X = 0
START_Y = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    # Define a method to create the ball object
    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(START_X, START_Y)

    # Define a method to move the ball diagonally across the screen
    def move(self):
        new_x = self.xcor() + 5
        new_y = self.ycor() + 5
        self.goto(new_x, new_y)







