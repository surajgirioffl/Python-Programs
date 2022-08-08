import turtle

t = turtle.Turtle()  # creating instance of class 'Turtle'
turtle.Screen().bgcolor("black")  # changing the background color to black
t.pencolor("red")
t.pensize(8)
t.speed(0)


radius = 100
# drawing


def halfCircle(color=t.pencolor()):
    """
    draw half circle. Take an argument of color of half circle. Default is the default color used in this module.
    """
    saveColor = t.pencolor()
    t.pencolor(color)  # user passed pencolor or default
    t.circle(radius, 90)
    t.circle(radius, -180)
    t.pencolor(saveColor)  # revert to original pen color


halfCircle("yellow")
t.penup()
t.left(90)
t.forward(radius)
t.pendown()
t.circle(5)
t.penup()
t.home()

turtle.done()
