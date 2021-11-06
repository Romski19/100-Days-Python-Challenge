from turtle import Turtle, Screen
import pandas
from scoreboard import Scoreboard

state_name = Turtle()
score_board = Scoreboard()
screen = Screen()

screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.bgpic(image)
df = pandas.read_csv("50_states.csv")
all_state = df.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
                data_dict = {
                    "Not Guessed States": missing_state
                }
                data = pandas.DataFrame(data_dict)
                data.to_csv("states_to_learn.csv")

        break
    if answer_state in all_state:
        guessed_state.append(answer_state)
        state_name.hideturtle()
        state_name.penup()
        state_data = df[df.state == answer_state]
        state_name.goto(int(state_data.x), int(state_data.y))
        state_name.write(f"{answer_state}")
        score_board.increase_score()

# states to learn





