import turtle
def circle1(r, c):
    turtle.color(c)
    turtle.right(90)
    turtle.penup()
    turtle.forward(r)
    turtle.pendown()
    turtle.left(90)
    for i in range(37):
        turtle.dot(7)
        turtle.circle(r, (360 / 37))

    turtle.penup()
    turtle.home()


def circle2(r, c):
    turtle.color(c)
    turtle.right(90)
    turtle.penup()
    turtle.forward(r)
    turtle.pendown()
    turtle.left(90)
    for i in range(37):
        turtle.dot(7)
        turtle.color('black')
        turtle.right(90)
        turtle.forward(20)
        turtle.backward(20)
        turtle.left(90)
        turtle.color(c)
        turtle.circle(r, (360 / 37))
    turtle.penup()
    turtle.home()


def circle3(r):
    turtle.color('black')
    turtle.right(90)
    turtle.penup()
    turtle.forward(r)

    turtle.left(90)
    turtle.circle(r, 5)
    for i in range(37):
        turtle.pendown()
        turtle.write(i, align='center')
        turtle.penup()
        turtle.circle(r, (360 / 37))

    turtle.penup()
    turtle.home()