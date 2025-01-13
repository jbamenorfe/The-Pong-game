"""This module creates the paddle Class. 13.01.2025"""

from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.x_pos = x_position
        self.y_pos = y_position
        self.create_paddle()

    # Define a method to create the paddle object
    def create_paddle(self):
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(self.x_pos, self.y_pos)

    # Define a method to move the paddle Up by 20px
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.x_pos, new_y)

    # Define a method to move the paddle Down by 20px
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.x_pos, new_y)