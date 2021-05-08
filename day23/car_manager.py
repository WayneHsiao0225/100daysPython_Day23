COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
import time
class Car():
    def __init__(self):
        ##super().__init__()
        self.cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create(self):
        #new_car=Turtle.shape("square")  ????
        new_car=Turtle("square")
        new_car.shapesize(stretch_wid=1,stretch_len=2)
        new_car.penup()
        #new_car.setheading(270)
        new_car.color(random.choice(COLORS))
        y=random.randint(-300,300)
        new_car.goto(250,y)
        self.cars.append(new_car)
    def move(self):
        for i in self.cars:
            i.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT










