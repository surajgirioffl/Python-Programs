# drawing cube using turtle graphics
import turtle
t = turtle.Turtle()  # creating object 't' of class 'Turtle'
t.pensize(5)
t.pencolor("black")
t.speed(6)

# defining function for drawing square

edge = 100  # edge of cube
diagonal = 2**0.5*edge


def drawSquare():
    for i in range(2):
        t.forward(edge)
        t.left(90)  # 90 degrees left
        t.forward(edge)
        t.left(90)  # 90 degrees left


# start drawing cube
drawSquare()
t.forward(edge/2)
t.left(90)  # 90 degrees left
# t.pencolor("white")  # changing the pencolor to white to make line invisible
t.penup()
t.forward(edge/2)
t.pendown()
drawSquare()

t.right(135)
t.forward(diagonal/2)
t.left(135)
t.forward(edge)

t.left(45)
t.forward(diagonal/2)
t.left(45)
t.forward(edge)

t.left(135)
t.forward(diagonal/2)
t.right(45)
t.forward(edge)

t.right(135)
t.forward(diagonal/2)

# end
turtle.done()
