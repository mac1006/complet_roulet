import time
import turtle


def circle1(r, c):
    turtle.color(c)
    turtle.right(90)
    turtle.penup()
    turtle.forward(r)
    turtle.pendown()
    turtle.left(90)
    for i in range(4):
        turtle.dot(7)
        turtle.circle(r, 90)
    turtle.penup()
    turtle.home()
    #time.sleep(3)

def circle2(r, c):
    turtle.color(c)
    turtle.right(90)
    turtle.penup()
    turtle.forward(r)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(r, 30)
    for i in range(4):
        turtle.dot(7)
        turtle.circle(r, 90)
    turtle.penup()
    turtle.home()
    #time.sleep(3)

def circle3(r, c):
    turtle.color(c)
    turtle.right(90)
    turtle.penup()
    turtle.forward(r)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(r, 60)
    for i in range(4):
        turtle.dot(7)
        turtle.circle(r, 90)
    turtle.penup()
    turtle.home()

circle1(50, 'green')
circle1(75, 'red')
circle1(100, 'blue')
circle2(50, 'green')
circle2(75, 'red')
circle2(100, 'blue')
circle3(50, 'green')
circle3(75, 'red')
circle3(100, 'blue')
time.sleep(3)