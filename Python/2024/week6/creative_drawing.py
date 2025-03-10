from turtle import Turtle, colormode, exitonclick, onscreenclick
from random import randint

timmy = Turtle()
timmy.shape("turtle")
colormode(255)
timmy.speed(100)


# let's add some psychedelic fun!
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


# draw some circles
def spirograph(tilt, extent):
    timmy.pensize(5)
    for _ in range(360 // tilt):
        timmy.pencolor(random_color())
        # timmy.begin_fill()
        timmy.circle(100, extent, extent // 3)
        # timmy.end_fill()
        timmy.left(tilt)


# draw some polygons
def geometry_fig(num, star=False):
    timmy.pensize(5)
    timmy.color(random_color(), random_color())
    dist = 100
    if num == 3:
        timmy.pencolor("red")  # for a red triangle
    if star and num % 2:
        dist *= 3
        angle = 180 / num - 180
    else:
        angle = 360 / num
    timmy.begin_fill()
    for _ in range(num):
        timmy.forward(dist)
        timmy.left(angle)
    timmy.end_fill()


# brownian motion
class Brownian:
    def __init__(self, minspeed, maxspeed):
        self.minspeed = minspeed
        self.maxspeed = maxspeed
        timmy.penup()
        timmy.goto(0, 0)
        timmy.pendown()
        timmy.pensize(3)
        self.running = True
        onscreenclick(self.stop, 1)

    def stop(self, x, y):
        self.running = False

    def run(self):
        while self.running:
            timmy.speed(randint(self.minspeed, self.maxspeed))
            timmy.pencolor(random_color())
            timmy.right(randint(0, 359))
            timmy.forward(randint(0, 20))


if __name__ == "__main__":
    timmy.penup()
    timmy.backward(200)
    timmy.pendown()
    spirograph(15, 365)
    timmy.penup()
    timmy.setheading(0)
    timmy.forward(300)
    timmy.pendown()
    for n in range(12, 2, -1):
        geometry_fig(n)
    timmy.penup()
    timmy.right(90)
    timmy.forward(300)
    timmy.setheading(72)
    timmy.pendown()
    geometry_fig(5, True)
    Brownian(5, 25).run()
    exitonclick()
