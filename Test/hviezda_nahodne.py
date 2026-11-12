import turtle
from random import randrange as nahodne

t = turtle.Pen()


def hviezda(luc):
    for i in range(10):
        t.fd(luc)
        t.bk(luc)
        t.rt(36)


screen = turtle.Screen()
screen.bgcolor("navy")
t.pencolor("yellow")

for i in range(10):
    x = nahodne(-300, 300)
    y = nahodne(-300, 300)
    t.pu()
    t.setpos(x, y)
    t.pd()
    luc = nahodne(5, 25)
    hviezda(luc)
    turtle.delay(1)

turtle.exitonclick()
