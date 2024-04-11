# a turtle screen is opened with the bg image of the US
# there is a loop that asks to choose a state
# if the state exists and not already picked, write the state in the coordinates

from turtle import Turtle, Screen
import time
import pandas as pd

screen = Screen()
screen.bgpic("blank_states_img.gif")

writer = Turtle()
writer.hideturtle()
writer.penup()

state_information = pd.read_csv("50_states.csv")
state_series = state_information.state
print(type(state_information))
chosen_states = []


def write_state_on_screen(choice):
    appropriate_row = state_information[state_series == choice]
    xcor = appropriate_row.x.iloc[0]
    ycor = appropriate_row.y.iloc[0]
    writer.goto(xcor, ycor)
    writer.write(choice, align="center")




# ask user for input
# if input is in state name series, call write function with the x and y coordinates of that index

cont = True
while cont:
    choice = screen.textinput("Guess a US state. Type 'exit' to leave.", "Your guess:").title()

    if choice in state_series.to_list() and choice not in chosen_states:

        chosen_states.append(choice)
        write_state_on_screen(choice)

    elif choice == "Exit":
        break

final_dataframe = pd.DataFrame({
    'Chosen states': chosen_states
})
final_dataframes = pd.DataFrame({
    'Missed states': list(set(state_series.to_list()) - set(chosen_states))
})

finals_dataframes = pd.concat([final_dataframe, final_dataframes])

finals_dataframes.to_csv("Result")
print(chosen_states)