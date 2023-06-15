import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def print_state(answer_state):
    guessed_states.append(answer_state)
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    print(state_data)
    t.write(state_data.state.item())


data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"Guess the state {len(guessed_states)}/50",
        prompt="What's another state's name?",
    ).title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv",header=["state"],index=False)

        break

    if answer_state in all_states:
        print_state(answer_state)

