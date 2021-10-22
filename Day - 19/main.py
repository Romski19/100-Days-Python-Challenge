from turtle import Screen, Turtle

screen = Screen()
bao = Turtle()


def move_forward():
    bao.forward(10)


def move_backward():
    bao.backward(10)


def move_right():
    bao.right(10)


def move_left():
    bao.left(10)


def go_clear():
    bao.clear()
    bao.penup()
    bao.home()
    bao.pendown()



screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(go_clear, "c")

screen.exitonclick()
