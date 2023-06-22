import turtle

def draw_sierpinski(length, depth):
    if depth == 0:
        # Base case: draw a single triangle
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        # Recursive case: draw three smaller triangles
        draw_sierpinski(length / 2, depth - 1)
        turtle.forward(length / 2)
        draw_sierpinski(length / 2, depth - 1)
        turtle.backward(length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        draw_sierpinski(length / 2, depth - 1)
        turtle.left(60)
        turtle.backward(length / 2)
        turtle.right(60)

# Set up the turtle graphics window
turtle.speed(0)  # Fastest speed
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()

# Call the function to draw the Sierpinski triangle
draw_sierpinski(400, 4)

# Keep the window open until it is manually closed
turtle.done()
