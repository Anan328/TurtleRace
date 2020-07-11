import turtle
from random import *
import time
# handling errors if any
try:
# creating turtle screen

    turtle.title("Turtle Race-Designed By ANAN")
    s=turtle.Screen()
    s.cv._rootwindow.resizable(False,False)
    s.setup(600,600)
    s.bgcolor("green")
    turtle.penup()
    turtle.speed(0)
    turtle.goto(-100,250)
    turtle.write("Turtle Race-Designed By ANAN",font=("vijaya",15,"bold"))
    # creating dirt
    turtle.setpos(-290,-200)
    turtle.pendown()
    turtle.color("chocolate")
    turtle.begin_fill()
    turtle.forward(590)
    turtle.right(90)
    turtle.forward(97)
    turtle.right(90)
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(97)
    turtle.end_fill()

    # finish line
    turtle.penup()
    turtle.shape("square")
    turtle.color("white")
    #turtle.shapesize(15/20)
    for i in range(10):
        turtle.setpos(200,200-(i*20*2))
        turtle.stamp()
    for j in range(10):
        turtle.setpos(200+20,200-20-(j*20*2))
        turtle.stamp()
    turtle.pendown()
    # creating turtles
    # turtle1
    turtle1 = turtle.Turtle()
    turtle1.speed(0)
    turtle1.shape("turtle")
    turtle1.color("yellow")
    turtle1.penup()
    turtle1.setpos(-250,0)
    turtle1.pendown()
    turtle1.pensize(3)

    # turtle2
    turtle2 = turtle.Turtle()
    turtle2.speed(0)
    turtle2.shape("turtle")
    turtle2.color("magenta")
    turtle2.penup()
    turtle2.setpos(-250,80)
    turtle2.pendown()
    turtle2.pensize(3)

    # turtle3
    turtle3 = turtle.Turtle()
    turtle3.speed(0)
    turtle3.shape("turtle")
    turtle3.color("red")
    turtle3.penup()
    turtle3.setpos(-250,150)
    turtle3.pendown()
    turtle3.pensize(3)

    # turtle4
    turtle4 = turtle.Turtle()
    turtle4.speed(0)
    turtle4.shape("turtle")
    turtle4.color("black")
    turtle4.penup()
    turtle4.setpos(-250,-80)
    turtle4.pendown()
    turtle4.pensize(3)

    # add a little pause
    time.sleep(1)



    for i in range(175):
        turtle1.forward(randint(0,5))
        turtle2.forward(randint(0, 5))
        turtle3.forward(randint(0, 5))
        turtle4.forward(randint(0, 5))

    turtle.exitonclick()
except Exception:
    pass