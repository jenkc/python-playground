import turtle
import math

bob = turtle.Turtle()
print(bob)


# move methods
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)

# function to draw a square
# def draw_square():
# 	for i in range(4):
# 		bob.fd(100)
# 		bob.lt(90)

# 4.3 Exercises
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

# square(bob, 100)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        
# polygon(bob, 100, 5)
        
def circle(t, rad):
    circumference = 2 * math.pi * rad
    n = 50
    length = circumference / n
    polygon(t, n, length)
    
# circle(bob, 50)

def arc(t, rad, angle):
    


turtle.mainloop()