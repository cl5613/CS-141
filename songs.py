"""
Use functions to draw a song based on the letters using five colors.
file name: songs.py
author: Chen Lin
"""
import turtle as tt

def draw_square():
    """
    simply draw a square
    """
    tt.forward(10)
    tt.left(90)
    tt.forward(10)
    tt.left(90)
    tt.forward(10)
    tt.left(90)
    tt.forward(10)
    tt.left(90)
    tt.forward(10)


def square(color):
    """
    param: color
    draw squares with filled color
    """
    tt.color(color)
    tt.begin_fill()
    draw_square()
    tt.end_fill()
    

def paint_line(line):
    """
    param : line
    each character will be one of the five colors
    """
    for ch in line :
        if ord(ch) < 70 and ord(ch) >= 0:
            color = 'red'
            square(color)
        elif ord(ch) >= 70 and ord(ch) < 100:
            color = 'yellow'
            square(color)
        elif ord(ch) >= 100 and ord(ch) <110:
            color = 'green'
            square(color)
        elif ord(ch) >= 110 and ord(ch) < 122:
            color = 'blue'
            square(color)
        elif ord(ch) >= 122:
            color = 'pink'
            square(color)
            
    
def picture():
    """
    This opens the file and draw the squares based on it
    """
    f = open('s2.txt')
    for line in f:
        print(line)
        tt.up()
        tt.goto(-300,300)
        tt.down()
        paint_line(line)
    f.close()


def main():
    """
    draw squares using five colors based on letters in the song
    """
    tt.tracer(0,0)
    picture()

main()


    
    
    

    
            
