import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US States Game")

# Create the background image for the game
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Use pandas to get all the states
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    # Get the user answer using the textinput
    answer_state = screen.textinput(
        title="Guess The State", prompt="What's another state name?: ")

    # Check if the user answer is in the all_states list
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)

screen.exitonclick()
