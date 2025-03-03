import turtle

def draw_square(t, x, y, color, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def draw_checkered_board(rows, cols, size):
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    turtle1 = turtle.Turtle()
    turtle2 = turtle.Turtle()
    turtle1.speed(0)
    turtle2.speed(0)
    
    colors = ["black", "red"]
    
    for row in range(rows):
        for col in range(cols):
            x = col * size - (cols * size) // 2
            y = (rows * size) // 2 - row * size
            color = colors[(row + col) % 2]
            if color == "black":
                draw_square(turtle1, x, y, color, size)
            else:
                draw_square(turtle2, x, y, color, size)

    screen.mainloop()


draw_checkered_board(8, 8, 100)
