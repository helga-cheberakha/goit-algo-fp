import math
import turtle

def draw_square(t: turtle.Turtle, size: float) -> None:
  """
  Draw a square and return to the starting
  position and direction.
  """
  for _ in range(4):
    t.forward(size)
    t.left(90)

def pythagoras_tree(t: turtle.Turtle, depth: int, size: float) -> None:
    """
    Draw a Pythagoras tree recursively.
    """
    if depth <= 0:
        return

    # Save the position and direction before drawing the branch.
    start_position = t.position()
    start_heading = t.heading()

    draw_square(t, size)

    # Move to the top-left corner of the square.
    t.left(90)
    t.forward(size)
    t.right(90)

     # Each child square has half the area of its parent.
    new_size = size / math.sqrt(2)

    # Draw the left branch at a 45-degree angle.
    t.left(45)
    pythagoras_tree(t, depth - 1, new_size)

    # Move to the triangle top corner and draw
    # the right branch.
    t.forward(new_size)
    t.right(90)
    pythagoras_tree(t, depth - 1, new_size)

    # Restore the starting state without drawing
    # a connecting line.
    t.penup()
    t.goto(start_position)
    t.setheading(start_heading)
    t.pendown()

def draw_pythagoras_tree(depth: int, size: float = 100) -> None:
    """
    Open a window and draw a Pythagoras tree.
    """
    if depth <= 0:
        raise ValueError("Depth must be a positive integer.")

    if size <= 0:
        raise ValueError("Size must be positive.")

    window = turtle.Screen()
    window.title("Pythagoras tree")
    window.setup(width=1000, height=800)
    window.bgcolor("white")
    window.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    # Place the trunk near the bottom of the window.
    t.penup()
    t.goto(-size / 2, -window.window_height() / 2 + 50)
    t.pendown()

    pythagoras_tree(t, depth, size)
    window.update()

    # Keep the window open until the user closes it.
    window.mainloop()
