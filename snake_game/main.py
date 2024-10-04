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
    food_x_pos = abs(food.get_position()[0])
    food_y_pos = abs(food.get_position()[1])
    print(f'Food pos is {food_x_pos}')
    while game_is_on:
        screen.update()
        time.sleep(0.08)
        snake.move()
        snake_x_pos = abs(snake.get_position()[0])
        snake_y_pos = abs(snake.get_position()[1])

        if snake_x_pos ==  300 or snake_y_pos == 300:
            game_over()
            break
        elif snake.get_position() == food.get_position():
            game_over()
            break
            




    # Keep the window open until it is closed by the user
    screen.exitonclick()

if __name__ == "__main__":
    main()