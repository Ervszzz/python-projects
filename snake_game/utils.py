from turtle import Screen, Turtle

def is_close(pos1, pos2, distance=2):
    return abs(pos1[0] - pos2[0]) < distance and abs(pos1[1] - pos2[1]) < distance

def setup_screen(screen):
    screen.clear()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

def clear_everything(screen):
    # Hide and clear all existing turtles to remove them from the screen
    for turtle in screen.turtles():
        turtle.hideturtle()
        turtle.clear()

    # Reset the screen
    screen.clearscreen()
    screen.bgcolor("black")
    screen.title("Snake Game")


def game_over():
    text_writer = Turtle()
    text_writer.hideturtle()  # We don't want to see the turtle, just the text
    text_writer.penup() 
    text_writer.goto(0, 0) # Move the turtle to the center of the screen
    text_writer.color("white")    
    text_writer.write("GAME OVER!!!! Play again? Y/N", align="center", font=("Arial", 16, "normal"))