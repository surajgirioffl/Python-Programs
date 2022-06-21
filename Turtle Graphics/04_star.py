import turtle
t = turtle.Turtle()  # creating object name 't' of class Turtle
t.speed(5)

length = 200
# drawing star
# start
for i in range(5):
    t.forward(length)
    t.left(144)  # 144 degrees left
# end
turtle.done()
