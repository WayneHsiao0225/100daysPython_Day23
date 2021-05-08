import time
from turtle import Screen
from player import Player
from car_manager import  Car
import random

from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car=Car()
scoreboard=Scoreboard()

screen.listen()
#screen.onkeyrelease(player.goup,"Up")
screen.onkeypress(player.goup,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    i=random.randint(1,10)
    if i==5:
        car.create()
    car.move()

    for i in car.cars:
        if i.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()
    if player.goal():
        player.restart_position()
        car.level_up()
        scoreboard.score_up()

screen.exitonclick() ###點擊 結束
