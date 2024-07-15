import turtle

write_turtle = turtle.Turtle()
write_turtle.color("red")

def show_msg(message):
    write_turtle.clear()
    write_turtle.write(message, False, align="right", font=('Arial', 16, 'normal'))



