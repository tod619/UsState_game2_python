import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US States Game")

# Create the background image for the game
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


screen.exitonclick()
