#importing required libraries
import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import ScoreBoard
import random

#initializing required variables
game_is_on = True
speed = 10

#initializing screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

#creating list to store cars
cars = []

#initializing player and scoreboard
player = Player()
scoreboard = ScoreBoard()

while game_is_on:

    time.sleep(0.1)
    
    #creating cars
    for i in range(random.randint(-4,1)):
        cars.append(Cars()) #storing cars objects in a list
    
    for i in cars:
        
        #moving cars
        i.move(speed)
    
        #collision with cars
        if (i.distance(player)<20):
            scoreboard.game_over()
            game_is_on = False
        
        #removing cars that reached left end
        if(i.xcor()<-280):
            cars.remove(i)
            i.ht()
            del i
    
    #player complete a level
    if(player.ycor()>280):
        scoreboard.new_score() #updating scorecard
        player.start() #sending player to start position
        speed += 5 #increasing car max move distance
    
    #moving car on keypress
    screen.onkeypress(player.upward,"Up")
    screen.onkeypress(player.leftward,"Left")
    screen.onkeypress(player.rightward,"Right")
    screen.update()

screen.exitonclick()