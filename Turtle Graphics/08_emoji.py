import turtle
# creating instance of class 'Turtle' from file 'turtle'.Starting With Python (Foundation)/01_Input & Output/calculator.
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.pencolor("white")
t.shape("turtle")
turtle.Screen().bgcolor("black")
turtle.setup(600, 820)
# def drawMouth():


def drawEye(angle):
    t.pencolor("black")
    t.penup()
    t.left(angle)
    t.forward(radius/1.5)
    t.pendown()
    t.circle(5)


radius = 200
t.begin_fill()
t.fillcolor("yellow")
t.circle(radius)
t.end_fill()

t.penup()
t.left(90)
t.forward(radius)
savePosition = t.position()
drawEye(45)

t.penup()
t.setposition(savePosition)
t.pendown()
drawEye(270)

t.penup()
t.setposition(savePosition)
t.pendown()

t.left(210)
t.forward(radius/4)
t.left(110)
t.forward(radius/6)
t.penup()

t.goto(0, 0)
t.left(90)
t.forward(radius/4.5)

t.right(65)
t.forward(radius/1.5)
t.left(45)
t.pendown()
# - for starting drawing circle to right else + for left
t.circle(radius/2, -155)


t.hideturtle()
turtle.done()
