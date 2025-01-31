import random
import os
import turtle
import time

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def Say(text):
    print(text)

def Add(n1, n2):
    return(n1 + n2)

def Subtract(n1, n2):
    return(n1 - n2)

def Multiply(n1, n2):
    return(n1 * n2)

def Divide(n1, n2):
    return(n1 / n2)

def Random(n1, n2):
    return(random.randint(n1, n2))

def Wait(secs):
    time.sleep(secs)

def NewDrawCanvas(turtleColor = "black", bgColor = "white", speed = 1, thickness = 1):
    global t
    global t_s

    t = turtle.Turtle()
    t_s = turtle.Screen()
    
    t_s.bgcolor(bgColor)
    t.speed(speed)
    t.pensize(thickness)
    t.color(turtleColor)

def DrawSquare(side=10):
    for i in range(4):
        t.forward(side*10)
        t.left(90)

def DrawCircle(radius=10):
    t.circle(radius*10)

def MovePen(x_off,y_off):
    t.penup()
    curX = t.xcor()
    curY = t.ycor()
    t.goto(curX+x_off,curY+y_off)
    t.seth(0)
    t.pendown()

def DrawLine(length=10):
    t.forward(length*10)

def RotTurtle(deg=90):
    t.right(deg)

def ChangeColor(clr):
    t.color(clr)

def ClearDrawCanvas():
    t.clear()

def EndDrawCanvas():
    t_s.exitonclick()

