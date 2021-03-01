# import colorgram
#
#
# def extract_rgb_from_image(image_name, number_of_colors):
#     rgb_colors = []
#     for color in colorgram.extract(image_name, number_of_colors):
#         # print(color.rgb[r])
#         rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
#         # colors.append(color.rgb)
#     return rgb_colors
#
#
# # print(colorgram.extract("image.jpg", 250))
#
# print(extract_rgb_from_image("image.jpg", 30))
import turtle as t
import random

colors = [(216, 148, 92), (221, 78, 57), (45, 94, 146), (151, 64, 91), (232, 219, 93), (217, 65, 85), (22, 27, 41),
          (40, 22, 29), (120, 167, 197), (40, 19, 14), (194, 139, 159), (159, 72, 56), (35, 132, 91), (123, 181, 142),
          (69, 167, 94), (236, 222, 6), (170, 176, 42), (231, 168, 182), (14, 30, 21), (51, 54, 105), (106, 42, 61),
          (25, 168, 202), (236, 171, 161), (107, 44, 37), (163, 210, 185), (150, 207, 222)]


timmy = t.Turtle()
t.colormode(255)
timmy.penup()
timmy.hideturtle()
timmy.speed("fastest")
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.hideturtle()


def draw_hirst_painting(num_of_rows, number_of_dots_per_each_row, dot_size, distance_between_dots):
    for _ in range(num_of_rows):
        for _ in range(number_of_dots_per_each_row):
            timmy.pencolor(random.choice(colors))
            timmy.dot(dot_size)
            timmy.forward(distance_between_dots)
        timmy.setheading(90)
        timmy.forward(distance_between_dots)
        timmy.setheading(180)
        timmy.forward(distance_between_dots * number_of_dots_per_each_row)
        timmy.setheading(0)


draw_hirst_painting(10, 10, 30, 50)


screen = t.Screen()
screen.exitonclick()
