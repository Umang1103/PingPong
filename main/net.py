from turtle import Turtle

class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.goto(0,-290)
        self.color("white")
        self.draw()

    def draw(self):
        while self.ycor() < 290:
            self.width(4)
            self.seth(90)
            self.fd(5)
            self.pu()
            self.fd(5)
            self.pd()
            
            