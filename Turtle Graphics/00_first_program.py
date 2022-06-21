import turtle
# To create object of a class, we use "objName = <fileName>.className()"
obj = turtle.Turtle()  # creating object of Turtle class
obj.pensize(3)
obj.pencolor('blue')
obj.speed(10)


sObj = turtle.Screen()  # creating object of Screen class
sObj.title("Suraj kumar Giri")
sObj.bgcolor('white')

for i in range(10):
    obj.circle(50)
    obj.forward(50)
    obj.left(50)
turtle.done()
