import turtle
t = turtle.Turtle()  # creating object name 't' of class Turtle

# sides of square/rectangle (for square, length == breadth)
length = 200
breadth = 200
# drawing square
# start
for i in range(2):
    print(i)
    t.forward(length)
    t.left(90)  # 90 degrees left
    t.forward(breadth)
    t.left(90)  # 90 degrees left

# end
turtle.done()
