from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("CAPSTONE PROJECT Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        screen.update()
        time.sleep(1)

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        screen.update()
        time.sleep(1)


screen.exitonclick()