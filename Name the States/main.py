import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
state_names = states.state.to_list()
guessed_states = []

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in state_names:
            if state not in guessed_states:
                missing_states.append(state)
        missing_states_df = pandas.DataFrame(missing_states)
        missing_states_df.to_csv("States to learn")
        break
    if answer_state in state_names:
        guessed_states.append(answer_state)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()

        state_data = states[states.state == answer_state]
        new_turtle.goto(int(state_data.x), int(state_data.y))
        new_turtle.write(answer_state)


