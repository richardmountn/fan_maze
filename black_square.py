import turtle
import keyboard
import random

import player
import texting

maze_drawer_turtle = turtle.Turtle()
maze_drawer_turtle.speed(0)
maze_drawer_turtle.color('black')
maze_drawer_turtle.fillcolor('black')

cell_size = 10

gamer_1 = player.Player(cell_size, 2, 1)

def create_cell(x, y):
    
    maze_drawer_turtle.begin_fill()
    maze_drawer_turtle.penup()
    maze_drawer_turtle.goto(x * cell_size, y * cell_size)

    step = 0
    while True:
        maze_drawer_turtle.forward(cell_size)
        maze_drawer_turtle.right(90)
        step = step + 1
        if(step == 4):
            break
    maze_drawer_turtle.pendown()
    maze_drawer_turtle.end_fill()

maze = [
    [1,0,0,1,1,1,1,1,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,0,0,1,1,0,0,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
]

maze_height = len(maze)
maze_width = len(maze[0])

for y in range(maze_height):
    for x in range(maze_width):
        if(maze[y][x] == 1):
            create_cell(x,-y)

maze_drawer_turtle.hideturtle()


coins_turtle = turtle.Turtle()
coins_turtle.speed(0)
coins_turtle.color('black', 'yellow')

coins_num = random.randrange(1, 10)

def create_coins(x, y, c_s):
    
    coins_turtle.begin_fill()
    coins_turtle.penup()
    coins_turtle.goto(x * c_s + 5, y * c_s - 10)

    coins_turtle.circle(5)

    coins_turtle.pendown()
    coins_turtle.end_fill()



real_coins_num = 0

while(real_coins_num < coins_num):
    coins_pos_x = random.randrange(0, maze_width)
    coins_pos_y = random.randrange(0, maze_height)

    if maze[coins_pos_y][coins_pos_x] != 1 and maze[coins_pos_y][coins_pos_x] != 2:
        create_coins(coins_pos_x, -coins_pos_y, cell_size)
        maze[coins_pos_y][coins_pos_x] = 2
        real_coins_num += 1

    
coins_turtle.hideturtle()

texting.show_msg(f"{coins_num - real_coins_num} out of {coins_num}")

def can_move(x, y):
    if x < 0:
        return False

    if x >= maze_width:
        return False

    if y < 0:
        return False
    
    if y >= maze_height:
        return False
    
    if maze[y][x] == 1:
        return False
    
    return True

while True:
    if keyboard.is_pressed("escape"):
        exit()
    
    if keyboard.is_pressed('right'):
        if can_move(gamer_1.whatsright(), gamer_1.player_pos_y):
            gamer_1.move_right() 
    elif keyboard.is_pressed('left'):
        if can_move(gamer_1.whatsleft(), gamer_1.player_pos_y):
            gamer_1.move_left()
        
    if keyboard.is_pressed('up'):
        if can_move(gamer_1.player_pos_x, gamer_1.whatsup()):
            gamer_1.move_up()   
    elif keyboard.is_pressed('down'):
        if can_move(gamer_1.player_pos_x, gamer_1.whatsdown()):
            gamer_1.move_down()
    
    if maze[gamer_1.player_pos_y][gamer_1.player_pos_x] == 2:
        
        coins_turtle.color("white")
        create_coins(gamer_1.player_pos_x, -gamer_1.player_pos_y, cell_size)
        real_coins_num -= 1
        maze[gamer_1.player_pos_y][gamer_1.player_pos_x] = 0

        texting.show_msg(f"{coins_num - real_coins_num} out of {coins_num}")
    
    if real_coins_num == 0:
        break


texting.show_msg("You won!")

turtle.done()


