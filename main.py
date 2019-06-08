from turtle import Screen
from board import Board
from snake import Snake
width = 200
height = 150

screen = Screen()
screen.setup(width=width+500, height=height+400, startx=-1, starty=0)
screen.delay(0)

border = Board(width, height)

snake = Snake(screen, border, 40)
screen.onkey(snake.moveup, "Up")
screen.onkey(snake.movedown, "Down")
screen.onkey(snake.moveright, "Right")
screen.onkey(snake.moveleft, "Left")
snake.score()
snake.start()
screen.listen()
screen.mainloop()
