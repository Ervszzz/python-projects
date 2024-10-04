from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food

def game_over():
    text_writer = Turtle()
    text_writer.hideturtle()  # We don't want to see the turtle, just the text
    text_writer.penup() 
    text_writer.goto(0, 0) # Move the turtle to the center of the screen
    text_writer.color("white")    
    text_writer.write("GAME OVER!!!!", align="center", font=("Arial", 16, "normal"))

def is_close(pos1, pos2, distance=2):
    return abs(pos1[0] - pos2[0]) < distance and abs(pos1[1] - pos2[1]) < distance

def main():
    screen = Screen() # Create the Screen
    screen.setup(width=600, height=600) # Define the dimensions of the screen
    screen.bgcolor("black") # Set the background color
    screen.title("Snake Game") # Set the title
    screen.tracer(0)


    snake = Snake() # Create the Snake
    screen.listen() # Set the screen to listen for inputs
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


    game_is_on = True
    food = Food()
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
            snake.add_segment()
            food.remove_food()
            food.create_food() # Create new food


if __name__ == "__main__":
    main()