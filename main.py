from turtle import Screen
from snake import Snake
import time
from scoreboard import scoreBoard
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
score = scoreBoard()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 \
            or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
        # score.gameover()
        # game_is_on = False

    # detect body collision
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            #game_is_on = False
            #score.gameover()
            score.reset()
            snake.reset()

screen.exitonclick()
