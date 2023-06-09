# Day 18: The Hirst Painting Project

# import colorgram

# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [
    (201, 164, 112),
    (238, 246, 241),
    (150, 75, 49),
    (221, 201, 138),
    (52, 93, 124),
    (170, 153, 41),
    (139, 31, 19),
    (134, 163, 184),
    (197, 93, 73),
    (48, 123, 87),
    (73, 44, 35),
    (145, 178, 148),
    (14, 99, 71),
    (233, 175, 164),
    (161, 142, 158),
    (35, 61, 75),
    (236, 224, 4),
    (49, 72, 66),
    (107, 127, 153),
    (182, 205, 175),
    (19, 85, 110),
    (46, 66, 86),
    (77, 74, 39),
    (165, 97, 119),
    (91, 147, 129),
    (5, 68, 52),
    (109, 140, 161),
    (40, 59, 65),
]

tim.setheading(225)
tim.forward(300)

tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()