from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from utils import *
screen = Screen() # Create the Screen


def play_again():
    # It's crucial to stop listening to key events during reset to avoid issues.
    screen.onkey(None, "y")  # Disable the handler to prevent multiple restarts
    screen.clearscreen()  # Clears the current Turtle graphics and state
    main()  # Restart the game
    screen.listen()  # Start listening for key events again
    screen.onkey(play_again, "y")  # Rebind the play_again function to "y"



def main():
    setup_screen(screen)
    snake = Snake() # Create the Snake
    food = Food()   # Create the food
    scoreboard = Scoreboard() # Create the scoreboard

    screen.listen() # Set the screen to listen for inputs

    # Bind Controls
    screen.onkey(snake.up, "Up") 
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    screen_boundary = 300 - 10
    
    while game_is_on:
        screen.update()
        time.sleep(0.08)
        snake.move()

        snake_x_pos = abs(snake.get_position()[0]) # Get the absolute value of x coordinate
        snake_y_pos = abs(snake.get_position()[1]) # Get the absolute value of y coordinate

        # Main game loop adjustments
        if snake_x_pos >= screen_boundary or snake_y_pos >= screen_boundary:
            game_is_on = False
            clear_everything(screen)
            game_over()
            screen.onkey(play_again, "y")
            screen.onkey(exit, 'n')
        elif is_close(snake.get_position(), food.get_position(), distance=20):  # Assuming a tolerance of 20
            scoreboard.score = len(snake.segments) - 3
            scoreboard.increment_score()
            screen.update()
            snake.add_segment()
            food.remove_food()
            food.create_food() # Create new food

        # Check if snake eats its own tails
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_is_on = False
                clear_everything(screen)
                game_over()
                screen.onkey(play_again, "y")
                screen.onkey(exit, 'n')
    
    screen.exitonclick()


if __name__ == "__main__":
    main()