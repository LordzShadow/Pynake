from turtle import Screen, Turtle
from random import randint
width = 200
height = 150

screen = Screen()
head = Turtle()
body = Turtle()
apple = Turtle()
screen.delay(0)
size = 40
points = 0
body.pencolor("white")
body.hideturtle()
apple.hideturtle()
texter = Turtle()
texter.hideturtle()
texter.penup()

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

def score():
    texter.setpos(0, bordery + 100)
    texter.pendown()
    texter.clear()
    texter.write("Score:" + str(points), align="center", font=("Arial", 12, "normal"))
    texter.penup()

def restart():
    global size
    texter.clear()
    size = 40
    score()
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
    global points
    texter.setpos(0, 0)
    texter.color("red")
    texter.write("YOU DEAD", font=("Arial", 40, "normal"), align="center")
    texter.setpos(0, -100)
    texter.write("Press 'r' to start over", font=("Arial", 15, "normal"), align="center")
    points = 0

def updateSnake():
    global size
    global points

    off = 5
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
    if ax-off < hx < ax+off and ay-off < hy < ay+off:

        size += 10
        points += 10
        score()
        apple.clear()
        apple.penup()
        apple.setpos(randint(-borderx + 5, borderx - 5), randint(-bordery + 5, bordery - 5))
        while apple.pos() in posarr:
            apple.setpos(randint(-borderx + 5, borderx - 5), randint(-bordery + 5, bordery - 5))
        apple.pendown()
        apple.dot()


    posarr.append((hx, hy))
    if len(posarr) > size:
        body.setpos(posarr[0])
        posarr.pop(0)
    screen.ontimer(updateSnake, 10)


borderx, bordery = Board(width, height)
apple.penup()
apple.pencolor("red")
texter.pencolor("red")
apple.setpos(randint(-borderx + 5, borderx - 5), randint(-bordery + 5, bordery - 5))
apple.pendown()
apple.dot()
screen.onkey(moveup, "Up")
screen.onkey(movedown, "Down")
screen.onkey(moveright, "Right")
screen.onkey(moveleft, "Left")

score()
screen.ontimer(updateSnake, 500)
screen.listen()
screen.mainloop()
