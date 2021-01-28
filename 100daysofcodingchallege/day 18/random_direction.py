import turtle as t
import random
from turtle import Screen

tim=t.Turtle()
colours=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
directions=[0,90,180,270]
tim.pensize(12)
tim.speed(0)

for _ in range (200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading((random.choice(directions)))
screen=Screen()
screen.exitonclick()