import turtle
from turtle import Turtle, Screen
import  random
is_race_on=False
screen= Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make your Bet",prompt="which turtle will win the Race?Enter a color: ")
colors=["red", "orange", "yellow", "green", "blue", "purple"]
print(user_bet)
value=[-80,-40,0,40,80,120]
all_turtles=[]
for turtle_index in range(0,6) :
    new_turtle= Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=value[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        RD=random.randint(0,10)
        turtle.forward(RD)

screen.exitonclick()