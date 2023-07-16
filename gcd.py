"""
Use tail-recursive and iterative function to find GCD
file name: gcd.py
author: Chen Lin
"""

def gcd_rec(a,b):
    """
    This function will use tail-recursive to find GCD of two numbers
    param a: (positive int)
    param b: (positive int)
    """
    if b == 0:
        return a
    elif b < 0:
        pass
    else:
        return gcd_rec(b, a % b)
    
gcd_rec(5,5)


def test_gcd_rec():
    """
    This function tests the tail-recursive above.
    """
    print( 'Choose one and type it below to test its GCD:' )
    print( 'gcd_rec(5,5)' )
    print( 'gcd_rec(10,5)' )
    print( 'gcd_rec(5,10)' )
    print( 'gcd_rec(1,4)' )
    print( 'gcd_rec(4,1)' )
    print( 'gcd_rec(6,9)' )
     
test_gcd_rec()


def gcd_iter(a,b):
    """
    This function will use iteration to find GCD of the two numbers
    param a: (positive int)
    param b: (positive int)
    """
    while b > 0:
        tmp = a
        a = b
        b = tmp % b
    return a

gcd_iter(5,5)


def test_gcd_iter():
    """
    This function tests the iteration above.
    """
    print( 'gcd_iter(1,3)' )
    print( 'gcd_iter(3,1)' )
    print( 'gcd_iter(4,2)' )
    print( 'gcd_iter(6,18)' )
    print( 'gcd_iter(18,6)' )
    print( 'gcd_iter(9,9)' )

test_gcd_iter()
    

        

    
