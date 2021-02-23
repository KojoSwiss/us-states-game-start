import turtle
import pandas

screen = turtle.Screen()
screen.title("US States")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
guesses = []


us_states = pandas.read_csv("50_states.csv")
states_list = us_states.state.to_list()

while len(guesses) < 50:
    answer = screen.textinput(prompt="Guess the state", title=f"{len(guesses)}/50 correct").title()
    if answer == "Exit":
        states_missed = []
        for state in states_list:
            if state not in guesses:
                states_missed.append(state)
        df = pandas.DataFrame(states_missed)
        df.to_csv("Must_learn.csv")
        for m_state in states_missed:
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            state_row = us_states[us_states.state == m_state]
            x = int(state_row.x)
            y = int(state_row.y)
            t.goto(x, y)
            t.color("red")
            t.write(m_state)
        break

    if answer in states_list and answer not in guesses:
        guesses.append(answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        answer_row = us_states[us_states.state == answer]
        x = int(answer_row.x)
        y = int(answer_row.y)
        t.goto(x, y)
        t.write(answer)

screen.mainloop()
