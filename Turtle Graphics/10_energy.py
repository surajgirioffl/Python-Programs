import turtle
from random import randint
t = turtle.Turtle()  # creating instance of class Turtle
sc = turtle.Screen()  # creating instance of class '_Screen' via Screen global function
sc.bgcolor("black")
t.speed(0)

radius = 50
width = 60  # width between two circles
sc.colormode(255)
t.penup()
t.left(90)
t.forward(radius)
t.pencolor("red")
t.dot(18)
center = t.position()
t.home()
t.pendown()

# to draw thd circles
for i in range(5):
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    t.pencolor((r, b, g))
    t.circle(radius)
    t.penup()
    t.right(90)
    t.forward(width)
    t.left(90)
    t.pendown()
    radius += width

t.penup()
t.goto(center)
lengthOfLine = 50+4*width  # 50 is the initial radius
t.pendown()

# to draw the spokes
while True:
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    t.pencolor((r, g, b))
    t.forward(lengthOfLine)
    t.penup()
    t.backward(lengthOfLine)
    t.pendown()
    t.right(10)

turtle.done()
