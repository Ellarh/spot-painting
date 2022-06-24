# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('spot.jpg', 8)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
import random

color_list = [(172, 154, 70), (190, 30, 19), (244, 239, 226), (194, 166, 108), (135, 167, 193),
              (49, 102, 145), (145, 90, 43)]

tim = Turtle()
tim.shape("triangle")
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(15, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(360)
        tim.backward(500)
        tim.setheading(0)




my_screen = Screen()
my_screen.exitonclick()
