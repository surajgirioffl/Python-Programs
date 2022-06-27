import turtle
t = turtle.Turtle()  # creating object of class Turtle()
t.pensize(2)
t.speed(0)
t.pencolor("yellow")
turtle.Screen().bgcolor("black")  # calling function bgcolor() of class Screen()

# drawing
i = int()
while(i < 125):
    t.circle(i)
    t.left(10)
    t.forward(40)
    i += 1

turtle.done()
