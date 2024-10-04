from turtle import Screen, Turtle
import random
SCREEN_DIMENSION = (580,580)

class Food():
    def __init__(self):
        self.food = None
        self.position = None
        self.create_food()

    def create_food(self):
        new_food = Turtle("circle")
        new_food.color("blue")
        new_food.penup()
        new_food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food = new_food
        grid_size = 20
        x_max = SCREEN_DIMENSION[0]//2 // grid_size
        y_max = SCREEN_DIMENSION[1]//2 // grid_size
        random_x = random.randint(-x_max, x_max) * grid_size
        random_y = random.randint(-y_max, y_max) * grid_size

        # Spawn location in the screen
        new_food.goto(random_x, random_y)

    def get_position(self):
        return self.food.pos()


