"""
use turtle graphics to draw a bowtie
file name: bowties.py
author: Chen Lin
"""

import turtle as tt

size = 100

def draw_one_bowtie(size):
    """
    this function will draw the largest bowtie at the center
    :param size: the size of the bowtie
    precondition: turtle is at the center, facing east.
    postcondition: turtle is at the center, facing east.
    """
    tt.screensize(600,600)
    tt.pencolor("Blue")
    tt.pendown()
    tt.left(30)
    tt.forward(size)
    tt.right(120)
    tt.forward(size)
    tt.right(120)
    tt.forward(size*2)
    tt.left(120)
    tt.forward(size)
    tt.left(120)
    tt.forward(size)
    tt.right(120)
    tt.penup()
    tt.forward(size/4)
    tt.left(90)
    tt.pendown()
    tt.begin_fill()
    tt.circle(size/4)
    tt.color("red")
    tt.end_fill()
    tt.left(90)
    tt.forward(size/4)
    tt.right(90)
    

def draw_bowtie0(size):
    """
    :param size: the size of the bowtie
    this is depth 0 where there is no bowties drawn
    precondition: turtle is at the center, facing east.
    postcondition: turtle is at the center, facing east.
    """
    pass

def draw_bowtie1(size):
    """
    :param size: the size of the bowtie
    this is depth 1 where there is one largest bowtie drawn at the center
    precondition: turtle is at the center, facing east.
    postcondition: turtle is at the center, facing east.
    """
    tt.speed(10)
    draw_bowtie0(size)
    draw_one_bowtie(size)
    

def draw_bowtie2(size):
    """
    :param size: the size of the bowtie
    this is depth 2 where there is one largest bowtie and four small bowties.
    precondition: turtle is at the center, facing east.
    postcondition: turtle is at the center, facing east.
    """
    draw_bowtie1(size)
    tt.right(30)
    tt.penup()
    tt.forward(size*2)
    tt.pendown()
    draw_bowtie1(size/3) # finished first bowtie(size/3) at lower right
    tt.penup()
    tt.backward(size*4)
    tt.pendown()
    draw_bowtie1(size/3) # finished second bowtie(size/3) at upper left
    tt.penup()
    tt.forward(size*2)
    tt.left(60)
    tt.forward(size*2)
    tt.pendown()
    draw_bowtie1(size/3) # finished third bowtie(size/3) at upper right
    tt.penup()
    tt.backward(size*4)
    tt.pendown()
    draw_bowtie1(size/3) # finished fourth bowtie(size/3) lower left
    tt.penup()
    tt.forward(size*2)
    tt.right(30)
    
def draw_bowtie3(size):
    """
    :param size: the size of the bowtie
    this is depth 3 where there is one largest bowtie and four small bowties
    followed by four really small bowtie besides each of four small bowties.
    precondition: turtle is at the center, facing east.
    postcondition: turtle is at the center, facing east. 
    """
    tt.pencolor("Blue") # start the largest bowtie
    tt.pendown()
    tt.left(30)
    tt.forward(size)
    tt.right(120)
    tt.forward(size)
    tt.right(120)
    tt.forward(size*2)
    tt.left(120)
    tt.forward(size)
    tt.left(120)
    tt.forward(size)
    tt.right(120)
    tt.penup()
    tt.forward(size/4)
    tt.left(90)
    tt.pendown()
    tt.begin_fill()
    tt.circle(size/4)
    tt.color("red")
    tt.end_fill()
    tt.left(90)
    tt.forward(size/4)
    tt.right(90)    # finished the largest bowtie
    tt.right(30)
    tt.penup()
    tt.forward(size*2)
    tt.pendown()
    draw_bowtie2(size/3)    # finished the right lower five bowties
    tt.penup()
    tt.backward(size*4)
    tt.pendown()
    draw_bowtie2(size/3)    # finished the upper left five bowties
    tt.penup()
    tt.forward(size*2)
    tt.left(60)
    tt.forward(size*2)
    tt.pendown()
    draw_bowtie2(size/3)    # finished the upper right five bowties
    tt.penup()
    tt.backward(size*4)
    tt.pendown()
    draw_bowtie2(size/3)    # finished the lower left five bowties
    tt.penup()
    tt.forward(size*2)
    tt.right(30)
    

def draw_bowties(size, depth):
    """
    This function will recursively draw the bowties
    :param depth: The current depth of recursion
    :param size: The size of the bowtie
    Preconditions:
        depth >= 0, size > 0,
        turtle is facing east, pen down.
    Postconditions:
        bowties will drawn for the current depth,
        turtle is facing east, pen down.
    """
    if (depth == 0):
        pass
    else:
        draw_one_bowtie(size)
        tt.right(30)
        tt.penup()
        tt.forward(size*2)
        tt.pendown()
        draw_bowties(size/3, depth-1)
        tt.penup()
        tt.backward(size*4)
        tt.pendown()
        draw_bowties(size/3, depth-1)
        tt.penup()
        tt.forward(size*2)
        tt.left(60)
        tt.forward(size*2)
        tt.pendown()
        draw_bowties(size/3, depth-1)
        tt.penup()
        tt.backward(size*4)
        tt.pendown()
        draw_bowties(size/3, depth-1)
        tt.penup()
        tt.forward(size*2)
        tt.right(30)
           
        
def main():
    """
    This function allows you choose any depth to produce the image for that depth
    """
    depth = int(input( "Choose a depth:" ))
    tt.clear()
    draw_bowties(size, depth)
    print( "you can now close the window." )
    tt.done()

if __name__ == '__main__':
    main() 
        
    
