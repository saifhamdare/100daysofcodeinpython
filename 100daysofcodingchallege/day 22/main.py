from turtle import Turtle ,Screen
from scoreboard import Scoreboard
from pong import Pong
from ball import Ball
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong: The Game")
screen.tracer(0)

r_Pong=Pong((350,0))
l_Pong=Pong((-350,0))
ball =Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_Pong.up, "Up")
screen.onkey(r_Pong.down, "Down")
screen.onkey(l_Pong.up, "w")
screen.onkey(l_Pong.down, "s")

game_is_on= True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(r_Pong)<50 and ball.xcor()>320 or ball.distance(l_Pong)< 50 and ball.xcor()< -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()