import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move, "Up")
car = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.creat_car()
    car.moving()
    for i in car.all_car:
        if player.distance(i.pos()) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 290:
        player.refresh()
        car.update_car()
        scoreboard.update_level()
        car.car_refresh()

screen.exitonclick()
