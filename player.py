from turtle import Turtle
class Player(Turtle):
    
    #creating player
    def __init__(self):
        super().__init__("turtle")
        self.color("white")
        self.penup()
        self.start()
        self.setheading(90)
    
    #moving player for keypress
    def upward(self):
        self.forward(10)
    def leftward(self):
        self.goto(self.xcor()-10,self.ycor())
    def rightward(self):
        self.goto(self.xcor()+10,self.ycor())
    
    #sending player at start position
    def start(self):
        self.goto(0,-280)
    