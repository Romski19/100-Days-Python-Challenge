from turtle import *
import colorgram
screen = Screen()
tgp = Turtle()
screen.colormode(255)
tgp.fillcolor(252, 209,22)

tgp.begin_fill()
# first part
tgp.setheading(240)
tgp.forward(300)
tgp.setheading(125)
tgp.forward(300)
tgp.setheading(355)
tgp.forward(50)
tgp.setheading(305)
tgp.forward(200)
tgp.setheading(60)
tgp.forward(270)

#second part
tgp.setheading(135)
tgp.forward(270)
tgp.setheading(0)
tgp.forward(350)
tgp.setheading(300)
tgp.forward(40)
tgp.setheading(180)
tgp.forward(280)
tgp.setheading(315)
tgp.forward(230)

# third part
tgp.setheading(0)
tgp.forward(280)
tgp.setheading(245)
tgp.forward(340)
tgp.setheading(180)
tgp.forward(50)
tgp.setheading(65)
tgp.forward(290)
tgp.setheading(180)
tgp.forward(250)

tgp.end_fill()




screen.exitonclick()