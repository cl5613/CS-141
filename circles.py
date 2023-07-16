"""
Use turtle graphics to produce a non-recursive circle-drawing program that
draws circles within circles.
file name: circles.py
author: Chen Lin
"""
import turtle as tt

radius = 100
pen_size = 2

def init():
    """
    set up the turtle at the initial state.
    :precondition: turtle is at the center and facing east
    :postcondition: turtle is at the center and facing east
    """
    tt.setpos(0, 0)
    tt.speed(0)
    tt.pensize(pen_size)
    tt.down()

def draw_circles_0(radius):
    """
    No tree at depth 0.
    :precondition: turtle is at the center and facing east
    :postcondition: turtle is at the center and facing east
    """
    pass

def draw_circles_1(radius):
    """
    Depth 1 of circle is a 150 radius circle.
    :precondition: turtle is at the center and facing east
    :postcondition: turtle is at the center and facing east
    """
    tt.pensize(2)
    draw_circles_0(radius)
    tt.circle(radius)
    
def draw_circles_2(radius):
    """
    Depth 2 has three circles, a 150 radius big circle and two identical
    circles inside big circle.
    :precondition: turtle is at the center and facing east
    :postcondition: turtle is on the left of the circle and facing south
    """
    tt.pensize(2)
    tt.left(180)
    tt.circle(-radius,90)
    tt.right(180)
    draw_circles_1(radius/2)
    tt.circle(radius,90)
    tt.circle(radius,90)
    draw_circles_1(radius/2)
    tt.circle(radius,90)
    tt.circle(radius,90)

def draw_circles_3(radius):
    """
    Depth 3 contains a big circle, two middle circles and four small circles
    in the two middle circles.
    :precondition: turtle is on the left and facing south
    :postcondition: turtle is on the left and facing south
    """
    draw_circles_2(radius/2)
    tt.circle(radius/2,90)
    tt.circle(radius,90)
    tt.circle(radius,90)
    draw_circles_2(radius/2)
    tt.circle(radius/2,90)
    tt.circle(radius,90)
    tt.circle(radius,90)

def draw_circles_rec(radius, depth):
    """
    This function will recursively draw the circle.
    :param depth: (int) The current depth of recursion
    :param radius: (int) The radius of the current circle
    Preconditions:
        depth >= 0, radius > 0,
        turtle is facing east,
        turtle pen is down.
    Postconditions:
        circles were drawn for the current depth,
        turtle is facing east,
        turtle pen is down.
    """
    
    if (depth == 0):
        pass
    elif (depth >=1):
        tt.circle(radius)
        draw_circles_rec(radius/2,depth-1)
        tt.circle(radius,90)
        tt.circle(radius,90)
        draw_circles_rec(radius/2,depth-1)
        tt.circle(radius,90)
        tt.circle(radius,90)
        
def main():
    """
    This main function will let the program work by showing different depths.
    """
    init()
    print( "Drawing a depth-1 circles drawing." )
    draw_circles_1(radius)
    input( "Hit ENTER to proceed to depth 2:" )
    tt.clear()
    draw_circles_2(radius)
    input( "Hit ENTER to proceed to depth 3:" )
    tt.clear()
    draw_circles_3(radius)
    input( "Hit ENTER to proceed to recursive code:" )
    tt.clear()
    depth = int( input( "depth? " ) )
    draw_circles_rec(radius, depth)
    print( "Close the window to end the program." )
    tt.done()

if __name__ == '__main__':
    main()

        
        


    




