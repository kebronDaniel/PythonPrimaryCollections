import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
screen.title("U.S. States Game")
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()

write_state = turtle.Turtle()
write_state.hideturtle()
write_state.penup()

correct_answers = 0
found_states = []
while True:
    user_answer = screen.textinput(title=f"{correct_answers}/50 States Correct", prompt="What is another State's Name?") \
        .title()
    if user_answer == 'Exit':
        break
    if user_answer in states:
        row = data[data["state"] == user_answer]
        print(row)
        x_loc = int(row.x)
        y_loc = int(row["y"])
        write_state.goto(x_loc, y_loc)
        write_state.write(user_answer)
        correct_answers += 1
        print(f"{user_answer} is written")
        found_states.append(user_answer)


states_to_learn = [state for state in states if state not in found_states]

df = pandas.DataFrame(states_to_learn, columns=["States_to_learn"])
df.to_csv("states_to_learn.csv")

