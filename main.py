from operator import truediv
from turtle import Turtle,Screen
import pandas

def convert(str):
    l = ""
    count = 0
    for ch in str:
        count = count+1
        if ch == " ":
            count = 0
            l = l+" "
            continue
        if count==1:
            l=l+(ch.upper())
        else:
            l = l+ch
    return l

data = pandas.read_csv("50_states.csv")
screen = Screen()
tim = Turtle()

image =  "blank_states_img.gif"
screen.title("US STATES GAME")
screen.addshape(image)
tim.shape(image)
is_game_on = True
list = []


while len(list)<50:
    answer = screen.textinput(f"US GAME {len(list)}/50 states guessed",prompt = "Guess another state name?")
    if convert(answer)=="Exit":
        break
    if len(data[data["state"] == convert(answer) ])!=0 and convert(answer) not in list:
        t = Turtle()
        t.penup()
        t.hideturtle()

        t.goto(int(data[data["state"] == convert(answer)].x),int(data[data["state"] == convert(answer)].y))
        t.write(arg = convert(answer), move=False, align='left', font=('Arial', 8, 'normal'))
        list.append(convert(answer))

missed_states = []
for rows in data["state"]:
    if  rows not in list:
        missed_states.append(rows)
table = pandas.DataFrame(missed_states)
table.to_csv("remaining_states.csv")

screen.exitonclick()
