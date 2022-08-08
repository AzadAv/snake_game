from turtle import Screen
import time
from tkinter import *

from click import command

from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import Wall

def run_game():

    screen = Screen()  # creating the screen
    screen.setup(width=600, height=600)  # Setting up screen size
    screen.bgcolor("black")  # screen background color
    screen.title("My Snake Game")  # title of the screen
    screen.tracer(0)  # cleans the screen


    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    wall = Wall()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(snake.speed)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
            snake.speed_up()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 260 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()
            
        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    # screen.exitonclick()
    screen.mainloop()

run_game()