import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US States Game")

# Create the background image for the game
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(
    title="Guess The State", prompt="What's another state name?: ")


screen.exitonclick()
