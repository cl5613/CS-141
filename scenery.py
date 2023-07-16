import turtle as tt
"""
use turtle graphics to draw a house, a pine tree and a maple tree.
"""

def draw_maple_tree():
    """
    draw a maple tree using turtle graphics
    """
    tt.penup()
    tt.pencolor("green")
    tt.pensize(2)
    tt.setpos(45,0)
    tt.pendown()
    tt.forward(200)
    tt.left(180)
    tt.forward(100)
    tt.right(90)
    tt.forward(60)
    tt.right(90)
    tt.circle(0.4*60)
    tt.penup()

def draw_house():
    """
    draw a housing using turtle graphics
    """
    tt.setpos(45,0)
    tt.pencolor("cyan")
    tt.pendown()
    tt.left(90)
    tt.forward(100)
    tt.left(45)
    tt.forward(70)
    tt.left(90)
    tt.forward(70)
    tt.left(45)
    tt.forward(100)
    tt.left(90)
    tt.forward(100)
    tt.penup()

def draw_pine_tree():
    """
    draw a pine tree using turtle graphics
    """
    tt.setpos(-55,0)
    tt.left(180)
    tt.pencolor("green")
    tt.pendown()
    tt.forward(200)
    tt.left(180)
    tt.forward(100)
    tt.left(90)
    tt.forward(90)
    tt.right(90)
    tt.forward(0.3*90)
    tt.left(120)
    tt.forward(0.6*90)
    tt.left(120)
    tt.forward(0.6*90)
    tt.left(120)
    tt.forward(0.3*90)

def main():
    """
    Ask three questions and answers
    """
    input(str("Is there a house in the forest (y/n)? y"))
    input(str("At what position (1/2/3)? 2"))
    input(str("What color is the house? cyan"))

if __name__ == '__main__':
    draw_maple_tree()
    draw_house()
    draw_pine_tree()
    main()

  




