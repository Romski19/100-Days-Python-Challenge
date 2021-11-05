from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.colormode(255)

turtle.up()
turtle.goto(-140,-75)
turtle.down()
turtle.seth(-45)
turtle.color('red')
turtle.circle(200,90)
turtle.seth(45)
turtle.circle(200,90)



screen.exitonclick()