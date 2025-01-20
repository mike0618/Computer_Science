from turtle import Turtle, colormode, exitonclick
from random import randint
from polyangle import Polyangle


# random rgb colors
def random_color():
    r = randint(0, 225)
    g = randint(0, 225)
    b = randint(0, 225)
    return r, g, b


# TODO: draw polygons function
def draw_polygon(p: Polyangle):
    # init turtle and set some variables
    timmy = Turtle()
    timmy.shape("turtle")
    colormode(255)
    dist = 1000 // p.n  # to fit the polygon in the screen
    angle = p.exterior()
    timmy.begin_fill()
    timmy.pensize(3)
    timmy.color(random_color())
    if p.n > 20:
        timmy.speed(10)
    for _ in range(p.n):
        timmy.pencolor(random_color())
        timmy.forward(dist)
        timmy.left(angle)
    timmy.end_fill()
    timmy.penup()
    timmy.goto(0, -300)
    timmy.pencolor("slategray")
    timmy.write(p.__repr__(), True, "left", ("Arial", 24, "normal"))
    timmy.goto(-50, 0)


# TODO: get and check user input of number of sides, return int
def get_sides() -> int:
    while True:
        inp = input("Enter the number > 2 of sides ot the polygon: ").strip()
        if not inp.isdigit():
            print("Wrong input")
            continue
        num = int(inp)
        if num < 3:
            print("The number should be > 2")
            continue
        return num


# TODO: get and check user input of length, return float
def get_length() -> float:
    while True:
        inp = input("Enter the side length: ").strip().replace(",", "")
        if not inp.replace(".", "", 1).isdigit():
            print("Wrong input")
            continue
        num = float(inp)
        if num <= 0:
            print("The number should be positive")
            continue
        return num


# TODO: main function
def main():
    num = get_sides()
    length = get_length()
    polygon = Polyangle(num, length)
    draw_polygon(polygon)


if __name__ == "__main__":
    main()
    exitonclick()
