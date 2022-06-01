from turtle import Turtle
from random import choice


# Speed (random choice from the two when initiliazing for x and y coors):
STARTING_DIRECTION = [-10, 10]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('VioletRed4')
        self.penup()
        self.moving_speed = 0.1

        # Ballio will go in random direction each time
        self.x_dir = choice(STARTING_DIRECTION)
        self.y_dir = choice(STARTING_DIRECTION)

    def move(self):
        self.goto(self.xcor() + self.x_dir, (self.ycor() + self.y_dir))

        # Wall collision detection:
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_dir = -self.y_dir

    def bounce(self):
        self.x_dir = -self.x_dir
        self.moving_speed *= 0.7

    def serve(self):
        self.goto(0, 0)
        self.bounce()
        self.moving_speed = 0.1
