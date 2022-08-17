import turtle
sc = turtle.Screen()  # creating object of Screen class
sc.title("Indian National Flag")
turtle.setup(800, 850)  # setting up the screen size
t = turtle.Turtle()  # creating instance of 'Turtle' Class
t.speed(5)


def drawRectangle(length: float, breadth: float | int):
    """
    _summary_:
    function to draw rectangle shape using turtle graphics.

    Args(_int_,_int_):
    Take arguments of length and breadth of rectangle.
    """
    t.forward(length)
    t.left(90)
    t.forward(breadth)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(breadth)


t.penup()
t.goto(-120, 200)  # changing the position of turtle to start drawing
t.pendown()


length = 270
breadth = 80


def drawFlagStrip(color: str):
    """_summary_
    Function to draw the strip of flag with desired color filled

    Args:
        color (_string_):
        Takes arguments for color of strip.
    """
    t.fillcolor(color)
    t.begin_fill()
    drawRectangle(length, breadth)
    t.end_fill()


# drawing flag tricolor strip
drawFlagStrip("#ff9933")  # saffron color
t.forward(2*breadth)
t.left(90)
drawFlagStrip("#138808")  # green color


# drawing right sided line in white colored strip.
t.backward(breadth)
t.left(90)
t.forward(length)
t.left(90)
t.forward(breadth)
t.left(90)
t.forward(length/2)
t.pendown()
savePosition = t.pos()

# drawing Ashok Chakra
t.pensize(5)
t.pencolor("#000080")  # navy blue color
radius = 39
t.circle(radius)
t.pensize(2)
t.left(90)
t.penup()
t.forward(radius)
t.pendown()
t.dot(5)
t.pensize(1)
# 24 spokes
for i in range(24):
    t.forward(radius)
    t.penup()
    t.backward(radius)
    t.pendown()
    t.right(15)


# drawing stick of flag
t.setpos(savePosition)  # setting an absolute position
t.right(90)
t.pensize(7)
t.pencolor("black")
t.penup()
t.forward(length/2)
t.left(90)
t.backward(breadth)
t.pendown()
t.forward(7*breadth)
t.dot(13)  # drawing dot
t.pensize(1)  # returned to normal size of pen

t.hideturtle()
turtle.done()  # closing the screen after done with drawing
