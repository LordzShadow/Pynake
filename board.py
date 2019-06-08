from turtle import Turtle

class Board:
    def __init__(self, w, h):

        self.w = w
        self.h = h
        self.x = self.w / 2
        self.y = self.h / 2
        marker = Turtle()
        marker.hideturtle()
        marker.penup()
        marker.setpos(self.x, self.y)
        marker.pendown()
        marker.setpos(-self.x, self.y)
        marker.setpos(-self.x, -self.y)
        marker.setpos(self.x, -self.y)
        marker.setpos(self.x, self.y)