import turtle
t = turtle.Turtle()  # creating object name 't' of class Turtle
t.pensize(5)
t.pencolor("black")
t.speed(4)

instance = turtle.Screen()  # creating object of Screen class
instance.bgcolor("dodgerblue")
instance.title("Windows Logo")


def drawSquare(left=True):
    for i in range(4):
        t.begin_fill()
        t.forward(side)
        if(left):
            t.left(90)
        else:  # for right
            t.right(90)


side = 150  # side of square
# drawing of stair
# start
drawSquare()
drawSquare(False)
t.left(180)
drawSquare(False)
drawSquare()
# end
turtle.done()
