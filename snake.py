from turtle import Screen, Turtle
from random import randint
screen = Screen()
screen.screensize(250, 250)
head = Turtle()
body = Turtle()
apple = Turtle()
screen.delay(0)
size = 10
body.pencolor("white")
body.hideturtle()
apple.hideturtle()
texter = Turtle()
texter.hideturtle()
texter.penup()
apple.dot()

def Board(w, h):
    x = w/2
    y = h/2
    marker = Turtle()
    marker.hideturtle()
    marker.penup()
    marker.setpos(x, y)
    marker.pendown()
    marker.setpos(-x, y)
    marker.setpos(-x, -y)
    marker.setpos(x, -y)
    marker.setpos(x, y)
    return x, y

posarr = []

def moveup():
    if head.heading() != 270:
        head.seth(90)

def movedown():
    if head.heading() != 90:
        head.seth(270)

def moveleft():
    if head.heading() != 0:
        head.seth(180)

def moveright():
    if head.heading() != 180:
        head.seth(0)

def restart():
    global size
    texter.clear()
    size = 10
    head.penup()
    body.penup()
    head.clear()
    body.clear()
    head.home()
    body.home()
    posarr.clear()
    head.color("black")
    screen.onkey(None, "r")
    head.pendown()
    body.pendown()
    screen.ontimer(updateSnake, 500)

def startover():
    texter.setpos(0, 0)
    texter.color("red")
    texter.write("YOU DEAD", font=("Arial", 40, "normal"), align="center")
    texter.setpos(0, -100)
    texter.write("Press 'r' to start over", font=("Arial", 15, "normal"), align="center")

def updateSnake():
    global size

    head.forward(1)
    hx, hy = head.pos()
    hx = round(hx, 0)
    hy = round(hy, 0)

    if ((hx, hy) in posarr and (hx, hy) != posarr[-1]) or hx >= borderx or hx <= -borderx or hy >= bordery or hy <= -bordery:
        head.penup()
        head.color("red")
        print("ded")
        startover()
        screen.onkey(restart, "r")
        return None

    ax,ay = apple.pos()
    if ax-3 < hx < ax+3 and ay-3 < hy < ay+3:
        apple.clear()
        size += 10
        apple.penup()
        apple.setpos(randint(-borderx + 5, borderx - 5), randint(-bordery + 5, bordery - 5))
        apple.pendown()
        apple.dot()


    posarr.append((hx, hy))
    if len(posarr) > size:
        body.setpos(posarr[0])
        posarr.pop(0)
    screen.ontimer(updateSnake, 10)


borderx, bordery = Board(750, 500)
screen.onkey(moveup, "Up")
screen.onkey(movedown, "Down")
screen.onkey(moveright, "Right")
screen.onkey(moveleft, "Left")


screen.ontimer(updateSnake, 500)
screen.listen()
screen.exitonclick()
