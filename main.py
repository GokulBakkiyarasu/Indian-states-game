import turtle
import pandas
from scoreboard import ScoreBoard

# setting up the screen and adding the map to it.
screen = turtle.Screen()
screen.setup(height=650, width=600)
screen.title("India States Game")
map_image = "map.gif"
screen.addshape(map_image)
turtle.shape(map_image)

# setting up the scoreboard of the game
scoreboard = ScoreBoard()

should_continue = True
guessed_answer = []
# data required for the game got using pandas library
data = pandas.read_csv("map_data.csv")
state_list = data["state"].to_list()
xcor_list = data["x"].to_list()
ycor_list = data["y"].to_list()


def quit_game():
    to_continue = screen.textinput("", "Do you want to continue(yes/no): ")
    if to_continue is not None:
        if to_continue.lower() == "no":
            return "exit"
        elif to_continue.lower() == "yes":
            pass
    else:
        return "none"


while should_continue:
    answer_state = screen.textinput("Indian_states", "Guess The State")
    # setting exit command to get out of the game
    if answer_state == "":
        print(answer_state)
        continue
    elif answer_state is None:
        conform = quit_game()
        if conform == "exit":
            break
        if conform == "none":
            quit_game()

    else:
        if answer_state.title() in state_list:
            answer_state = answer_state.title()
            index_value = state_list.index(answer_state)
            pen = turtle.Turtle()
            pen.penup()
            pen.hideturtle()
            pen.goto(xcor_list[index_value], ycor_list[index_value])
            pen.write(answer_state, font=("Calibri", 11, "normal"))
            guessed_answer.append(answer_state)
            # score update
            if answer_state in state_list and guessed_answer.count(answer_state) < 2:
                scoreboard.inc_score()
            # finishing point of the game
            if scoreboard.current_score > 29:
                should_continue = False
                scoreboard.game_over()
# saving the not guessed states to a new file
not_guessed_answer = {"states": []}
for state in state_list:
    if state not in guessed_answer:
        not_guessed_answer["states"].append(state)
not_guessed_data = pandas.DataFrame(not_guessed_answer)
not_guessed_data.to_csv("not_guessed.csv")
