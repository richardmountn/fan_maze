import turtle
import random

coins_turtle = turtle.Turtle()
coins_turtle.speed(0)
coins_turtle.color('black', 'yellow')

coins_num = random.randrange(1, 200)

def create_coins(x, y, cell_size):
    
    coins_turtle.begin_fill()
    coins_turtle.penup()
    coins_turtle.goto(x * cell_size - 5, y * cell_size)

    coins_turtle.circle(5)

    coins_turtle.pendown()
    coins_turtle.end_fill()

for i in range(coins_num):
    coins_pos_x = random.randrange(0, 12)
    coins_pos_y = random.randrange(0, 12)
    create_coins(coins_pos_x, coins_pos_y, 10)

coins_turtle.hideturtle()


turtle.exitonclick()

