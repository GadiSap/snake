from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score




def play_snake ():
    """Plays the snake game"""
    #sets the screen object
    screen =Screen()
    screen.clear()
    screen.title("Snake")
    screen.setup(width = 600, height = 600)
    screen.bgcolor("black")
    screen.tracer(0)

    #set the snake, food and score objects
    snake = Snake()
    food = Food()
    score = Score()
    #sets the screen listen method to follow user input.
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    screen.update()

    # runs game
    game_on = True
    while game_on:
        game_on = snake.move() #will move and check for collision with wall or snake body. If collision will return False
        screen.update()
        time.sleep(0.1)

        #Detect collision with food
        if snake.head.distance (food) < 10:
            score.increase_score()
            food.refresh()
            snake.extend()
        # Ends the game if collision with wall or snake body
        if not game_on:
            if score.game_over():
                play_snake()
        # Ends the game if there is snake fill up screen
        if score.points >= 280:
            game_on = False
            if score.win():
                play_snake()

    screen.exitonclick()

play_snake()

