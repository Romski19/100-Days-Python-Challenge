from turtle import Screen, Turtle
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
your_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?:").lower()
colors = ["red","blue","pink","gray","green","black"]
y_pos = [-50, -20, 10, 40, 70, 100]
all_bbms = []


for turtle_index in range(0, 6):
    bbm = Turtle(shape="turtle")
    bbm.color(colors[turtle_index])
    bbm.penup()
    bbm.goto(x=-230, y=y_pos[turtle_index])
    all_bbms.append(bbm)

if your_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_bbms:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if your_bet == win_color:
                print(f"You won!{win_color} won the race!")
            else:
                print(f"You lost!{win_color} won the race!")

        turtle_distance = random.randint(0, 10)
        turtle.forward(turtle_distance)



# bato = Turtle(shape="turtle")
# bato.color(colors[1])
# bato.penup()
# bato.goto(x=-230, y=70)

# leni = Turtle(shape="turtle")
# leni.color(colors[2])
# leni.penup()
# leni.goto(x=-230, y=40)
#
# isko = Turtle(shape="turtle")
# isko.color(colors[3])
# isko.penup()
# isko.goto(x=-230, y=10)
#
# leody = Turtle(shape="turtle")
# leody.color(colors[4])
# leody.penup()
# leody.goto(x=-230, y=-20)
#
# ping = Turtle(shape="turtle")
# ping.color(colors[5])
# ping.penup()
# ping.goto(x=-230, y=-50)



screen.exitonclick()

