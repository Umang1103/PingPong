# PING PONG GAME

# ----------------------------------------

# TODO: 1. Create the screen.
# TODO: 2. Create and move a paddle.
# TODO: 3. Create another paddle.
# TODO: 4. Create the ball and make it move.
# TODO: 5. Detect collision with wall and bounce.
# TODO: 6. Detect collision with paddle.
# TODO: 7. Detect when paddle misses.
# TODO: 8. Keep score.

# --------------------------------------------

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from net import Net
import time

scr = Screen()
scr.setup(width=800, height=600)
scr.bgcolor("black")
scr.title("Pong")
scr.tracer(0)

paddle_left = Paddle((-370,0))
paddle_right = Paddle((370,0))
ball = Ball()
net = Net()
score_right = ScoreBoard((60,220))
score_left = ScoreBoard((-60,220))

scr.listen()

scr.onkey(key="w",fun=paddle_left.up)
scr.onkey(key="s",fun=paddle_left.down)

scr.onkey(key="Up",fun=paddle_right.up)
scr.onkey(key="Down",fun=paddle_right.down)

eog= True
while eog:
    time.sleep(0.1)
    scr.update()
    ball.move()

    # DETECT COLLISION WITH WALL
    if ball.ycor() > 260 or ball.ycor() < -260:
        # BALL NEEDS TO BOUNCE
        ball.bounce_y()

    # DETECT COLLISION WITH PADDLE
    if ball.distance(paddle_right) < 50 and ball.xcor() > 340:
        # BALL BOUNCES AFTER HITTING RIGHT PADDLE
        ball.bounce_x()
        score_right.shooter()
    
    if ball.distance(paddle_left) < 50 and ball.xcor() < -340:
        # BALL BOUNCES AFTER HITTING LEFT PADDLE
        ball.bounce_x()
        score_left.shooter()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.msg()
        eog = False

scr.exitonclick()