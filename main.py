import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()

scoreboard = ScoreBoard()

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.end_game()
        game_is_on = False

    #detect snake body collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.end_game()
            game_is_on = False
            break

screen.exitonclick()
