from turtle import Turtle, colormode, exitonclick
from random import randint


# random rgb colors
def random_color():
    r = randint(0, 225)
    g = randint(0, 225)
    b = randint(0, 225)
    return r, g, b


# draw polygons
def draw_polygon(num):
    # init turtle and set some variables
    timmy = Turtle()
    timmy.shape("turtle")
    colormode(255)
    dist = 1000 // num
    angle = 360 / num
    # polygon names
    polygons = {
        3: "Triangle",
        4: "Quadrilateral",
        5: "Pentagon",
        6: "Hexagon",
        7: "Heptagon",
        8: "Octagon",
        9: "Nonagon",
        10: "Decagon",
        11: "Hendecagon",
        12: "Dodecagon",
        13: "Tridecagon",
        14: "Tetradecagon",
        15: "Pentadecagon",
        16: "Hexadecagon",
        17: "Heptadecagon",
        18: "Octadecagon",
        19: "Enneadecagon",
        20: "Icosagon",
    }
    timmy.begin_fill()
    for _ in range(num):
        timmy.pensize(randint(3, 8))
        timmy.speed(randint(1, 5))
        timmy.color(random_color())
        timmy.pencolor(random_color())
        timmy.shapesize(randint(5, 20) / 10, randint(5, 20) / 10, randint(10, 30) / 10)
        timmy.forward(dist)
        timmy.left(angle)
    timmy.end_fill()
    # write the name of the polygon
    timmy.penup()
    timmy.goto(0, -50)
    msg = f"A {num} sided polygon"
    name = polygons.get(num)
    if name:
        msg = name
    timmy.write(msg, True, "left", ("Arial", 24, "normal"))
    timmy.goto(0, -60)


# get and check user input
def get_input():
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


def main():
    num = get_input()
    draw_polygon(num)


if __name__ == "__main__":
    main()
    exitonclick()
