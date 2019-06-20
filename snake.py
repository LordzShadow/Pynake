from random import randint
from turtle import Turtle

class Snake:

    def __init__(self, screen, border, size):
        self.head = Turtle()
        self.body = Turtle()
        self.texter = Turtle()
        self.apple = Turtle()

        self.body.pencolor("white")
        self.body.hideturtle()
        self.apple.hideturtle()
        self.texter.hideturtle()
        self.texter.penup()
        self.texter.color("red")

        self.screen = screen
        self.border = border
        self.posarr = []
        self.size = size
        self.points = 0
        self.highest = 0

        self.apple.penup()
        self.apple.setpos(randint(-border.x + 5, border.x - 5), randint(-border.y + 5, border.y - 5))
        self.apple.pencolor("red")
        self.apple.pendown()
        self.apple.dot()

    def start(self):

        self.texter.setpos(0, 0)
        self.texter.pendown()
        self.texter.write("Press SPACE to start", font=("Arial", 20, "bold"), align="center")
        self.texter.penup()
        self.screen.onkey(self.run, "space")

    def run(self):
        self.texter.clear()
        self.screen.onkey(None, "space")
        self.score()
        self.updateSnake()

    def updateSnake(self):
        off = 5
        self.head.forward(1)
        hx, hy = self.head.pos()
        hx = round(hx, 0)
        hy = round(hy, 0)

        if ((hx, hy) in self.posarr and (hx, hy) != self.posarr[-1])\
                or hx >= self.border.x or hx <= -self.border.x or hy >= self.border.y or hy <= -self.border.y:
            self.head.penup()
            self.head.color("red")
            self.startover()
            self.screen.onkey(self.restart, "r")
            return None

        ax, ay = self.apple.pos()
        if ax - off < hx < ax + off and ay - off < hy < ay + off:

            self.size += 10
            self.points += 10
            self.score()
            self.apple.clear()
            self.apple.penup()
            self.apple.setpos(randint(-self.border.x + 5, self.border.x - 5), randint(-self.border.y + 5, self.border.y - 5))
            while self.apple.pos() in self.posarr:
                self.apple.setpos(randint(-self.border.x + 5, self.border.x - 5), randint(-self.border.y + 5, self.border.y - 5))
            self.apple.pendown()
            self.apple.dot()

        self.posarr.append((hx, hy))
        if len(self.posarr) > self.size:
            self.body.setpos(self.posarr[0])
            self.posarr.pop(0)
        self.screen.ontimer(self.updateSnake, 10)

    def moveup(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def movedown(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def moveleft(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def moveright(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def score(self):
        self.texter.setpos(0, self.border.y + 100)
        self.texter.pendown()
        self.texter.clear()
        self.texter.write("Score:" + str(self.points), align="center", font=("Arial", 12, "normal"))
        self.texter.penup()

    def restart(self):
        self.texter.clear()
        self.size = 40
        self.score()
        self.head.penup()
        self.body.penup()
        self.head.clear()
        self.body.clear()
        self.head.home()
        self.body.home()
        self.posarr.clear()
        self.head.color("black")
        self.screen.onkey(None, "r")
        self.head.pendown()
        self.body.pendown()
        self.screen.ontimer(self.updateSnake, 500)

    def startover(self):
        if self.points > self.highest:
            self.highest = self.points
        self.texter.setpos(0, self.border.y+30)
        self.texter.color("red")
        self.texter.write("YOU DEAD", font=("Arial", 40, "normal"), align="center")
        self.texter.setpos(0, -self.border.y-40)
        self.texter.write("Highscore:"+ str(self.highest), font=("Arial", 20, "normal"), align="center")
        self.texter.setpos(0, -self.border.y-65)
        self.texter.write("Press 'r' to start over", font=("Arial", 15, "normal"), align="center")
        self.points = 0



