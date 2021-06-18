from turtle import *
import random

# turtle.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.color("DarkGreen")
# tim.pensize(5)
colors = ["aquamarine", "BlueViolet", "chartreuse", "chocolate2", "cyan",
          "DarkMagenta", "DeepPink", "DeepSkyBlue"]
directions = [0, 90, 180, 270]
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, b, g)
    return color


def draw_circle():
    r = 100
    tim.circle(r)


for x in range(72):
    draw_circle()
    tim.rt(5)
    tim.color(random.choice(colors))
    # tim.color(random_color())


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.fd(100)
        tim.rt(angle)


# for x in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(x)


# for x in range(200):
#     tim.color(random_color())
#     tim.setheading(random.choice(directions))
#     tim.fd(random.randint(5, 26))


screen = Screen()
screen.exitonclick()
