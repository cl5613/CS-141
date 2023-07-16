"""
    Task 1
    File: conditionals.py
    author: Chen Lin
"""
def divisible(a,b):
(a,b)=int(input(('(a,b):'))
    if a === b:
        return True
    elif a and b < 0:
        return None
    elif a != b:
        return False

print (divisible(a,b))

def run_divisible(a,b):
    
a=int(input("enter the number for a:"))
b=int(input("enter the number for b:"))
c=int(input("enter the number for c:"))
        
if a or b < 0:
    print('Inputs must be positive integers!')

elif a == b: 
    print(a, 'equals' b,)

elif a % b ==0:
    print(a, 'is evenly divisible by' b,)

elif a % b !=0:
    print(a, 'is not evenly divisible by' b,)


"""
    Task 2
    A program to check if 3 sides form a triangle
"""
def is_triangle(a,b,c):
(a,b,c)= int(input(('(a,b,c):'))
    if a and b < 0
        return None
    elif a and b >= 0 and a + b >= c
        return True
    elif a and b >= 0 and a + b < c
        return False

print (is_triangle)
    
def run_is_triangle(a,b,c):

a=int(input("enter the number for a:"))
b=int(input("enter the number for b:"))
c=int(input("enter the number for c:"))

if (a+b>=c):
    print(a, b, c, 'can form a triangle')
elif (a+b<c):
    print(a, b, c, 'can not form a triangle')

if __name__ == "__main__":
    main()

