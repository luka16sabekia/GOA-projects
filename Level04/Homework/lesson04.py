import turtle

# Create a screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle for drawing
pen = turtle.Turtle()

# Draw the palace
def draw_palace():
    pen.penup()
    pen.goto(-100, -100)
    pen.pendown()
    pen.color("orange")
    pen.begin_fill()
    for _ in range(4):
        pen.forward(200)
        pen.left(90)
    pen.end_fill()

# Draw the king
def draw_king():
    pen.penup()
    pen.goto(-30, -100)
    pen.pendown()
    pen.color("yellow")
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()

# Draw the queen
def draw_queen():
    pen.penup()
    pen.goto(30, -100)
    pen.pendown()
    pen.color("pink")
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()

# Draw the tower
def draw_tower():
    pen.penup()
    pen.goto(-80, 100)
    pen.pendown()
    pen.color("gray")
    pen.begin_fill()
    for _ in range(4):
        pen.forward(160)
        pen.left(90)
    pen.end_fill()

# Place the GOA flag on the tower
def draw_flag():
    pen.penup()
    pen.goto(-20, 180)
    pen.pendown()
    pen.color("green")
    pen.begin_fill()
    pen.forward(40)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(40)
    pen.left(90)
    pen.forward(100)
    pen.end_fill()

# Main function to draw everything
def main():
    draw_palace()
    draw_king()
    draw_queen()
    draw_tower()
    draw_flag()

    # Hide the turtle and display the drawing
    pen.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
