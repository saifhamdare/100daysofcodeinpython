from turtle import Turtle,Screen
import random
timmy=Turtle()
timmy.shape("square")
for _ in range (3):
    timmy.forward(100)
    timmy.right(120)

for _ in range (4):
    timmy.forward(100)
    timmy.right(90)

for _ in range(5):
    timmy.forward(100)
    timmy.right(72)

for _ in range(6):
    timmy.forward(100)
    timmy.right(60)

for _ in range(7):
    timmy.forward(100)
    timmy.right(51.42)

for _ in range(8):
    timmy.forward(100)
    timmy.right(45)

for _ in range(9):
    timmy.forward(100)
    timmy.right(40)

for _ in range(10):
    timmy.forward(100)
    timmy.right(36)

timmy.forward(400)
colours=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
def draw_shape(num_slides):
    angle=360/num_slides
    for _ in range(num_slides):
        timmy.forward(100)
        timmy.right(angle)
for shape_side in range(3,11):
    timmy.color(random.choice(colours))
    draw_shape(shape_side)

screen=Screen()
screen.exitonclick()