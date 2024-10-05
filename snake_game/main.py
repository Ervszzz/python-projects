from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen() # Create the Screen

def game_over():
    text_writer = Turtle()
    text_writer.hideturtle()  # We don't want to see the turtle, just the text
    text_writer.penup() 
    text_writer.goto(0, 0) # Move the turtle to the center of the screen
    text_writer.color("white")    
    text_writer.write("GAME OVER!!!! Play again? Y/N", align="center", font=("Arial", 16, "normal"))


def is_close(pos1, pos2, distance=2):
    return abs(pos1[0] - pos2[0]) < distance and abs(pos1[1] - pos2[1]) < distance

def main():
    screen.setup(width=600, height=600) # Define the dimensions of the screen
    screen.bgcolor("black") # Set the background color
    screen.title("Snake Game") # Set the title
    screen.tracer(0)

    snake = Snake() # Create the Snake
    food = Food()   # Create the food
    scoreboard = Scoreboard() # Create the scoreboard

    screen.listen() # Set the screen to listen for inputs
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
        if abs(snake_x_pos) >= screen_boundary or abs(snake_y_pos) >= screen_boundary:
            game_over()
            break
        # Checks if the snake has eaten the food
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
                game_over()
    
    screen.exitonclick()


if __name__ == "__main__":
    main()