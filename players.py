from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.color('VioletRed4')
        self.goto(position)

    def up(self):
        if self.ycor() != 260:
            self.goto(self.xcor(), (self.ycor() + 20))

    def down(self):
        if self.ycor() != -260:
            self.goto(self.xcor(), (self.ycor() - 20))
