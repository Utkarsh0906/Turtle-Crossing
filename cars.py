from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
class Cars(Turtle):
    
    #creating car
    def __init__(self):
        super().__init__("square")
        self.penup()
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
        self.goto(280,random.randint(-280,280,))
        self.setheading(180)
    
    #moving car for random distance
    def move(self,speed):
        self.fd(random.randint(0,speed))
    