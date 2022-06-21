import turtle
# To create object of a class, we use "objName = <fileName>.className()"
t = turtle.Turtle()  # creating object 't' of Turtle class
t.pencolor("blue")
t.pensize(4)
t.speed(1)

# length of sides of triangle
b = 200
p = 200
h = ((b**2)+(p**2))**0.5  # b**2=b^2

# drawing right angled triangle
# start
t.forward(b)  # base
t.left(90)  # 90 degrees
t.forward(p)  # perpendicular
t.left(135)  # 135 degrees
t.forward(h)  # hypotenuse (h=rootUnder(p^2+b^2))
# end
turtle.done()
