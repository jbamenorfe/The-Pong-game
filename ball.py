

from turtle import Turtle
START_X = 0
START_Y = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    # Define a method to create the ball object
    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(START_X, START_Y)


    # Define a method to move the ball diagonally across the screen
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Define a method to bounce the ball when it hits the top and bottom walls
    def bounce_y(self):
        self.y_move *= -1

    # Define a method to bounce the ball when it hits a paddle
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(START_X, START_Y)
        self.bounce_x()
        self.move_speed = 0.1






