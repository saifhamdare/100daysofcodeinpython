import turtle
import pandas
screen= turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_state=[]
while len(guessed_state)<50:
    answer_state = (screen.textinput(title=f"{len(guessed_state)}/50 Correct Answer ", prompt="What's another state's name? ")).title()
    if answer_state=="Exit":
        missing_state = []
        for state in state_list:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_Learn.csv")
        break
    if answer_state in state_list:
        guessed_state.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        position= data[data.state==answer_state]
        t.goto(int(position.x),int(position.y))
        t.write(position.state.item())
