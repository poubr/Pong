from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('thistle4')
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        self.clear()
        self.setposition(-100, 200)  # 100, 200 or 80, 220
        self.write(arg=self.left_score, move=False, align='center', font=('Helvetica', 50, 'normal'))
        self.setposition(100, 200)  # 100, 200 or 80, 220
        self.write(arg=self.right_score, move=False, align='center', font=('Helvetica', 50, 'normal'))

    def win(self):
        self.setposition(-20, 10)
        winner = 'LEFT'
        if self.right_score > self.left_score:
            winner = ' RIGHT'

        self.write(arg=f'GAME OVER!\n   {winner} WINS', move=False, align='center', font=('Helvetica', 50, 'normal'))
