import turtle as t
import random
from turtle import Screen

tim=t.Turtle()
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color = (r, g, b)
    return  random_color


tim.speed(0)
def draw_spirograph(size):
    for _ in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading((tim.heading()+size))
draw_spirograph(5)
screen=Screen()
screen.exitonclick()