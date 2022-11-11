import random
import turtle

tim = turtle.Turtle()

angles = [0, 90, 180, 270]
turtle.colormode(255)


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


def draw_dashed_line(len):
    count = len // 3
    for _ in range(0, count):
        tim.forward(5)
        tim.penup()
        tim.forward(5)
        tim.pendown()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def random_walk():
    tim.pensize(2)
    tim.speed('fastest')
    for _ in range(0, 100):
        tim.color(random_color())
        tim.right(random.choice(angles))
        tim.forward(20)


def draw_spirograph(turning_angle):
    tim.speed('fastest')
    for _ in range(int(360 / turning_angle)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+turning_angle)


screen = turtle.Screen()
screen.exitonclick()
