from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.xmove = 10
        self.ymove = 10

    def move(self):
        x = self.xcor()+self.xmove
        y = self.ycor()+self.ymove
        self.goto(x, y)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1

    def msg(self):
        self.pu()
        self.goto(0,0)
        self.write("GAME OVER!", move=False, align="center", font=("Courier",35,"normal"))

    
        
        

            

