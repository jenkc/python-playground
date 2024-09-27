
import math
import turtle

# parameters are three pairs or x and y coordinates (the three corners of the triangle) and a turtle object t
def draw_triangle(x1, y1, x2, y2, x3, y3, t):
    # go to start of triangle
    # take pen "up" off the virtual paper
    t.up()
    # set position of turtle to first point
    t.setpos(x1, y1)
    # set the pen "down" on the paper
    t.down()
    t.setpos(x2, y2)
    t.setpos(x3, y3)
    t.setpos(x1, y1)
    t.up()
    
def drawKochSF(x1, y1, x2, y2, t):
    # calculate the coordinates for all the points in the basic pattern
    d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    r = d / 3.0
    h = r * math.sqrt(3)/2.0
    p3 = ((x1 + 2 * x2)/3.0, (y1 + 2 * y2)/3.0)
    p1 = ((2 * x1 + x2)/3.0, (2 * y1 + y2)/3.0)
    c = (0.5 * (x1 + x2), 0.5 * (y1 + y2))
    n = ((y1 - y2)/d,(x2 - x1)/d)
    p2 = (c[0] + h * n[0], c[1] + h * n[1])
    
    # use recursion to break down the first-level flake into smaller versions
    # if the length of the flake is over 10 pixels
    if d > 10:
        # flake segment 1
        drawKochSF(x1, y1, p1[0], p1[1], t)
        # flake segment 2
        drawKochSF(p1[0], p1[1], p2[0], p2[1], t)
        # flake segment 3
        drawKochSF(p2[0], p2[1], p3[0], p3[1], t)
        # flake segment 4
        drawKochSF(p3[0], p3[1], x2, y2, t)
    else:
        # draw cone
        t.up()
        # p1 to p2 to p3
        t.setpos(p1[0], p1[1])
        t.down()
        t.setpos(p2[0], p2[1])
        t.setpos(p3[0], p3[1])
        # draw sides
        t.up()
        # A to p1
        t.setpos(x1, y1)
        t.down()
        t.setpos(p1[0], p1[1])
        t.up()
        # p3 to B
        t.setpos(p3[0], p3[1])
        t.down()
        t.setpos(x2, y2)
        
    
def main():
    print('Drawing the Koch Snowflake')
    # create the turtle object for drawing
    t = turtle.Turtle()
    # hide the turtle shape in the output
    t.hideturtle()
    # draw
    # draw_triangle(-100, 0, 0, -173.2, 100, 0, t)
    try:
        drawKochSF(-100, 0, 100, 0, t)
        drawKochSF(0, -173.2, -100, 0, t)
        drawKochSF(100, 0, 0, -173.2, t)
    except:
        print("Exception, exiting.")
        exit(0)
        
    # wait for user to click on screen
    turtle.Screen().exitonclick()
    
if __name__ == '__main__':
    main()