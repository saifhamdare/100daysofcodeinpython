import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()
color_list=[(179, 148, 129), (217, 215, 21), (163, 73, 164), (237, 28, 36), (34, 177, 76), (255, 174, 201), (0, 0, 0), (136, 0, 21), (127, 127, 127), (63, 72, 204), (0, 162, 232), (112, 146, 190), (255, 242, 0)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=101

for dot_count in range (1, number_of_dots):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen=turtle_module.Screen()
screen.exitonclick()