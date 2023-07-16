"""
    Use turtle graphic to draw a five point star
    file name: Five_Point_Star
    author: Chen Lin
"""

import turtle

def draw_triangle_left():
    """
    draw triangle left makes the turtle draw a triangle on the left
    """
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)

def draw_triangle_right():
    """
    draw triangle right makes the turtle draw a triangle on the right
    """
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)

def main():
    turtle.down()
    draw_triangle_left()
    turtle.right(50)
    draw_triangle_left()
    turtle.right(180)
    turtle.forward(100)
    turtle.left(17)
    draw_triangle_left()
    turtle.right(77)
    turtle.forward(100)
    turtle.right(70)
    turtle.forward(100)
    turtle.right(10)
    draw_triangle_right()
    turtle.right(180)
    turtle.forward(100)
    turtle.right(17)
    draw_triangle_right()

main()



