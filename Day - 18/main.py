import random
import colorgram
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
bugoy_nga_bao = Turtle()

# colors = ["tomato", "firebrick", "indigo", "GreenYellow", "tomato", "firebrick", "indigo", "GreenYellow"]

# bugoy_nga_bao.shape("turtle")


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

# spirograph

#
#
# def draw_spirograph(size_of_gap):
#     for x in range(int(360 / size_of_gap)):
#         bugoy_nga_bao.color(random_color())
#         bugoy_nga_bao.speed("fastest")
#         bugoy_nga_bao.setheading(bugoy_nga_bao.heading() + size_of_gap)
#         bugoy_nga_bao.circle(100)
#
# draw_spirograph(5)

# random direction
# direction = [0, 90, 180, 270]
# for _ in range(500):
#     bugoy_nga_bao.color(random_color())
#     bugoy_nga_bao.pensize(10)
#     bugoy_nga_bao.forward(20)
#     bugoy_nga_bao.speed("fastest")
#     bugoy_nga_bao.setheading(random.choice(direction))

# random color generator
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b

# Herst painting
# color picker
# colors = colorgram.extract('hers_paint.jpg', 30)
# r_g_b = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     r_g_b.append(new_color)
# print(r_g_b)

color_list = [(241, 218, 68), (220, 144, 88), (36, 102, 155), (166, 76, 48), (228, 87, 52), (152, 53, 76),
              (107, 171, 205), (209, 78, 108), (43, 49, 112), (25, 34, 73), (64, 36, 22), (29, 127, 83), (19, 55, 35),
              (132, 34, 65), (208, 135, 160), (25, 173, 137), (12, 96, 52), (128, 180, 156), (60, 28, 53),
              (155, 163, 63), (124, 34, 30), (18, 171, 189), (250, 223, 2), (102, 107, 171), (238, 167, 153),
              (223, 173, 186)]
random.seed()



# def make_stamp():
#     bugoy_nga_bao.setheading(random.randint(1, 360))
#     bugoy_nga_bao.dot(20, random.choice(color_list))
#     bugoy_nga_bao.stamp()

bugoy_nga_bao.penup()
bugoy_nga_bao.hideturtle()
bugoy_nga_bao.speed("fastest")

bugoy_nga_bao.setheading(225)
bugoy_nga_bao.forward(300)
bugoy_nga_bao.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots):
    bugoy_nga_bao.dot(10,random.choice(color_list))
    bugoy_nga_bao.forward(50)

    if dot_count % 10 == 0:
        bugoy_nga_bao.setheading(90)
        bugoy_nga_bao.forward(50)
        bugoy_nga_bao.setheading(180)
        bugoy_nga_bao.forward(500)
        bugoy_nga_bao.setheading(0)




screen.exitonclick()
