from turtle import Turtle, colormode, exitonclick
from random import randint
from math import cos, sin, radians

timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(5)
colormode(255)


def polar_to_cartesian(r, theta):
    """Convert polar coordinates (r, theta) to Cartesian (x, y)."""
    x = r * cos(radians(theta))
    y = r * sin(radians(theta))
    return x, y


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def fib():
    # fibonacci spiral (golden ratio approximation)
    a = b = 0.75  # turn the spiral to fit the golden one
    for _ in range(20):
        timmy.speed(a)
        timmy.circle(a, 90)
        a, b = a + b, a  # generate fib. numbers


def golden(b=0):
    # real golden ratio spiral
    f = 0.5 * 5**0.5 + 0.5  # the golden ratio
    # speed does not take effect, make calculations of x, y before drawing might help
    timmy.speed(500)
    timmy.pencolor("red")
    timmy.shape("circle")  # using goto without heading
    for a in range(0, 1440, 3):
        r = f ** (a / 90)  # golden spiral formula in polar coordinates.
        timmy.pensize(r // f)  # makes a beautiful effect
        x, y = polar_to_cartesian(r, a + b)  # b turns the spiral
        # timmy.setheading(a + 90)  # don't need it so much
        timmy.goto(x, y)
        if not a % 9:
            timmy.pencolor(random_color())


fib()
timmy.penup()
timmy.goto(0, 0)
timmy.pendown()
golden()
timmy.penup()
timmy.goto(0, 0)
timmy.pendown()
golden(180)
exitonclick()
