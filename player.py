import turtle

class Player:
    cell_size = 0

    player_pos_x = 0
    player_pos_y = 0

    user = turtle.Turtle()

    user.goto(5,5)
    user.shape("turtle")
    user.color("purple", "red")

    def __init__(self, c_s, p_x, p_y):
        self.cell_size = c_s
        self.player_pos_x = p_x
        self.player_pos_y = p_y
        self.user.goto(c_s/2 + p_x * c_s, -(c_s/2 + p_y * c_s))

    def move_right(self):
        self.user.setheading(0)
        self.user.forward(self.cell_size)
        self.player_pos_x += 1

    def move_left(self):
        self.user.setheading(180)
        self.user.forward(self.cell_size)
        self.player_pos_x -= 1

    def move_up(self):
        self.user.setheading(90)
        self.user.forward(self.cell_size)
        self.player_pos_y -= 1

    def move_down(self):
        self.user.setheading(-90)
        self.user.forward(self.cell_size)
        self.player_pos_y += 1

    def whatsleft(self):
        return self.player_pos_x - 1

    def whatsright(self):
        return self.player_pos_x + 1

    def whatsup(self):
        return self.player_pos_y - 1

    def whatsdown(self):
        return self.player_pos_y + 1

