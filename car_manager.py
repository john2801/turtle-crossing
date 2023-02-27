COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        self.all_car = []
        self.speed = STARTING_MOVE_DISTANCE

    def creat_car(self):
        make_car = random.randint(1, 6)
        if make_car == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300, random.randint(-250, 250))
            car.setheading(180)
            self.all_car.append(car)

    def moving(self):
        for i in self.all_car:
            i.forward(self.speed)

    def car_refresh(self):
        self.all_car = []

    def update_car(self):
        self.speed += STARTING_MOVE_DISTANCE
