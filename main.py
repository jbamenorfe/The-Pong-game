"""The program uses python's turtle module to create the pong game which is
the replica of a tennis ball game. By JBAmenorfe on the 13th January 2025"""

# Import the necessary modules
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Create the screen object
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

# Create the right paddle
right_paddle = Paddle(350, 0)

# Create the left paddle
left_paddle = Paddle(-350, 0)

# Create the ball object
ball = Ball()


screen.listen()
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)




# Call the screen.exitonclick() method
screen.exitonclick()