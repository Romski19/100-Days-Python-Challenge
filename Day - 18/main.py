from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

colors = ["tomato", "firebrick", "indigo", "GreenYellow", "tomato", "firebrick", "indigo", "GreenYellow"]
bugoy_nga_bao = Turtle()
bugoy_nga_bao.shape("turtle")


# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# x = 100
# y = 90
# v = 0
# for _ in range(4):
#     bugoy_nga_bao.forward(x)
#     bugoy_nga_bao.right(y)

# v = 0
# while v!= 100:
#     bugoy_nga_bao.forward(10)
#     bugoy_nga_bao.penup()
#     bugoy_nga_bao.forward(10)
#     bugoy_nga_bao.pendown()
#     v += 10

# for _ in range(15):
#     bugoy_nga_bao.forward(10)
#     bugoy_nga_bao.penup()
#     bugoy_nga_bao.forward(10)
#     bugoy_nga_bao.pendown()

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         bugoy_nga_bao.forward(100)
#         bugoy_nga_bao.right(angle)
#
#
# for shape_n in range(3, 11):
#     bugoy_nga_bao.color(random.choice(colors))
#     draw_shape(shape_n)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


bugoy_nga_bao.degrees(90)
bugoy_nga_bao.circle(90, 360)
bugoy_nga_bao.degrees(360)
bugoy_nga_bao.circle(90, 360)


# direction = [0, 90, 180, 270]
# for _ in range(500):
#     bugoy_nga_bao.color(random_color())
#     bugoy_nga_bao.pensize(10)
#     bugoy_nga_bao.forward(20)
#     bugoy_nga_bao.speed("fastest")
#     bugoy_nga_bao.setheading(random.choice(direction))


screen.exitonclick()
