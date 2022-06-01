import time
from turtle import Screen, Turtle
from ball import Ball
from players import Player
from score import Scoreboard

# Set winning score:
WINNING = 10

# Setting up Screen:
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('MistyRose')
screen.title('Pongy Bally Game')
screen.tracer(0)

# Setting up players (paddles), scoreboard, and ball:
l_player = Player((-380, 0))
r_player = Player((370, 0))
score = Scoreboard()
ball = Ball()

# Setting up controls:
screen.listen()
screen.onkey(l_player.up, "w")
screen.onkey(l_player.down, "s")
screen.onkey(r_player.up, "Up")
screen.onkey(r_player.down, "Down")

# Drawing middle of the field:
middle = Turtle()
middle.color('thistle4')
middle.hideturtle()
middle.penup()
middle.goto(0, 300)
middle.seth(270)
middle.width(5)
for i in range(600):
    middle.pendown()
    middle.forward(10)
    middle.penup()
    middle.forward(10)


def pongy_bally():
    game_on = True
    while game_on:

        ball.move()
        screen.update()
        time.sleep(ball.moving_speed)

        # Checking for player scoring
        # (players' starting position minus 20 so ball bounces on the edge,
        # and distance is 40, i.e. distance from the center of the player's)
        if ball.xcor() == 350 or ball.xcor() == - 360:
            if ball.distance(l_player) < 40 or ball.distance(r_player) < 40:
                if ball.xcor() == 350:
                    score.right_score += 1
                    score.update()
                else:
                    score.left_score += 1
                    score.update()
                ball.bounce()

        # If player does not pong the ball, it is served again:
        if ball.xcor() > 350:
            score.left_score += 1
            score.update()
            ball.serve()

        if ball.xcor() < -360:
            score.right_score += 1
            score.update()
            ball.serve()

        # If one player reaches score of twenty, game ends
        if score.left_score == WINNING or score.right_score == WINNING:
            score.win()
            middle.clear()
            game_on = False


if __name__ == "__main__":
    pongy_bally()

screen.exitonclick()
