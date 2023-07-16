"""
Use recursive and iterative function to draw triangles
file name: arrows.py
author: Chen Lin
"""
import turtle as tt

def draw_bounding_box():
    tt.penup()
    tt.goto(-200,-200)
    tt.pendown()
    tt.forward(400)
    tt.left(90)
    tt.forward(400)
    tt.left(90)
    tt.forward(400)
    tt.left(90)
    tt.forward(400)
    tt.left(90)
    tt.penup()
    tt.goto(0,0)

draw_bounding_box()

def draw_triangles(num_tri, side_len):
    """
    draw equilateral triangle
    """
    if num_tri == 0:
        return
    else:
        tt.forward(side_len)
        tt.left(30)
        return draw_triangles(num_tri-1, side_len-1)


def draw_figures_rec(num_tri, side_len, acc_len=0):
    """
    Recursively draws triangles. Will draw a triangle with side lengths of
    side_len, moves forward 10 units, then turns left and calls itself with
    side_len - 1 and num_tri - 1
    """
    if num_tri == 0:
        return acc_len
    else:
        draw_triangles(num_tri, side_len)
        tt.up()
        tt.forward(10)
        tt.left(30)
        tt.down()
        draw_figures_rec(num_tri-1, side_len-1, side_len+acc_len)


def draw_figures_iter(num_tri, side_len, acc_len):
    """
    Iteratively draws triangles. Will draw a triangle with side lengths of
    side_len, moves forward 10 units, then turns left and repeats after reducing
    side_len and num_tri by 1
    """
    acc_len = 0
    
    while num_tri > 0:
        draw_triangles(num_tri, side_len)
        tt.up()
        tt.forward(10)
        tt.left(30)
        tt.down()
        acc_len += side_len
        side_len -= 1
        num_tri -= 1

    return acc_len

def eq_tri_area(side_len):
    """
    calculate the area of the equilateral triangle
    """
    side_len = float(input("Enter side length of equilateral triangle to find area:"))
    area = (sqrt(3)/4 * (side_len * side_len)) * num_tri     
    return area

eq_tri_area(side_len)








    

   
        
        
    
