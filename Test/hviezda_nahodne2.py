from turtle import bgcolor, pencolor, fd, bk, rt, pu, setpos, pd, delay, exitonclick
from random import randrange as nahodne


def hviezda(luc):
    for i in range(10):
        fd(luc)
        bk(luc)
        rt(36)


bgcolor("navy")
pencolor("yellow")

for i in range(10):
    x = nahodne(-300, 300)
    y = nahodne(-300, 300)
    pu()
    setpos(x, y)
    pd()
    luc = nahodne(5, 25)
    hviezda(luc)
    delay(1)

exitonclick()
