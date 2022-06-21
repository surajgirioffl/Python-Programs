import turtle
t = turtle.Turtle()  # creating object name 't' of class Turtle
t.pencolor("red")
t.pensize(4)
t.speed(10)

# drawing of circle
# start
for i in range(360):
    t.forward(2)
    t.left(1)  # 1 degrees left
# end
turtle.done()
