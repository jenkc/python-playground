import turtle
import math
import random, argparse
import random
from PIL import Image
from datetime import datetime

class Spiro:
    # constructor 
    # NOTE: xc and yc are coordinates of center of Spiro 
    # col is color and l is pen's distance from smaller circle's center
    def __init__(self, xc, yc, col, R, r, l):
        # create turtle object
        self.t = turtle.Turtle()
        # set the cursor shape
        self.t.shape('turtle')
        # set the step in degrees
        self.step = 5
        # set the drawing complete flag
        self.drawingComplete = False
        
        # set the parameters
        self.setparams(xc, yc, col, R, r, l)
        
        # initialize the drawing
        self.restart()
        
    def setparams(self, xc, yc, col, R, r, l):
        # the Spirograph parameters
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        
        # reduce r/R to its smallest form by dividing the GCD
        gcdVal = math.gcd(self.r, self.R)
        # set periodicity (number of rotations)
        self.nRot = self.r//gcdVal
        # get ratio of radii
        self.k = r/float(R)
        # set the color (* means optional, so if specified?)
        self.t.color(*col)
        # set the current angle, start at 0
        self.a = 0
        
    def restart(self):
        """Reset the drawing parameters for the Spiro object and get into postion to draw another spiro."""
        # set the flag, indicates the object is ready to draw a new Spiro
        self.darwingComplete = False
        # show the turtle
        self.t.showturtle()
        # lift up the pen and go to the first point
        self.t.up()
        # create local variables names to keep code compact in equations
        R, k, l = self.R, self.k, self.l
        # reset initial value of angle of rotation to 0
        a = 0.0
        # calculate x,y coordinates using parametric equations and move pen/turtle there
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) + l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()
        
    def draw(self):
        # draw the rest of the points
        R, k, l = self.R, self.k, self.l
        # step is the degree of rotation, to change each iteration
        for i in range(0, 360*self.nRot + 1, self.step):
            a = math.radians(i)
            x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
            y = R*((1-k)*math.sin(a) + l*k*math.sin((1-k)*a/k))
            try:
                self.setpos(self.xc + x, self.yc + y)
            except:
                print("Exception, exiting.")
                exit(0)
        self.t.hideturtle()
        
    def update(self):
        # skip the rest of the steps if done
        if self.drawingComplete == True:
            return
        # increment the angle
        self.a += self.step
        # draw a step
        R, k, l = self.R, self.k, self.l
        # set the angle
        a = math.radians(self.a)
        x = self.R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = self.R*((1-k)*math.sin(a) + l*k*math.sin((1-k)*a/k))
        try:
            self.t.setpos(self.xc + x, self.yc + y)
        except:
            print("Exception, exiting.")
            exit(0)
        # if drawing is complete, set the flag
        if self.a >= 360*self.nRot:
            self.drawingComplete = True
            # drawing is now done, so hide the turtle cursor
            self.t.hideturtle()
    # clear everything
    def clear(self):
        # pen up
        self.t.up()
        # clear turtle
        self.t.clear()
            
class SpiroAnimator:
    # constructor
    def __init__(self, N):
        # set the timer value in milliseconds
        self.deltaT = 10
        # get the window dimensions
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        # initialize a restarting flag to indicate if a restart is in progress
        self.restarting = False
        # create N Spiro objects and add them to a list
        self.spiros = []
        for i in range(N):
            # generate random parameters
            rparams = self.genRandomParams()
            # set the spiro parameters (* indicates tuple unpacked and multiple arguments passed)
            spiro = Spiro(*rparams)
            # add the new spiro to the list
            self.spiros.append(spiro)
        # call update function after deltaT milliseconds to set animation in motion
        turtle.ontimer(self.update, self.deltaT)
        
    def genRandomParams(self):
        width, height = self.width, self.height
        R = random.randint(50, min(width, height)//2)
        r = random.randint(10, 9*R//10)
        l = random.uniform(0.1, 0.9)
        xc = random.randint(-width//2, width//2)
        yc = random.randint(-height//2, height//2)
        col = (random.random(),
               random.random(),
               random.random())
        return (xc, yc, col, R, r, l)
    
    def restart(self):
        """Restart the animation to draw a new set of spiros."""
        # ignore restart if already in the middle of restarting
        if self.restarting == True:
            return
        else:
            self.restarting == True
        for spiro in self.spiros:
            # clear
            spiro.clear()
            # generate new random parameters
            rparams = self.genRandomParams()
            # set the spiro parameters
            spiro.setparams(*rparams)
            # restart drawing
            spiro.restart()
        # done restarting
        self.restarting = False
        
    def update(self):
        """Called by the timer ever 10ms to update all the Spiro objects used by the animation."""
        # update all spiros
        nComplete = 0
        for spiro in self.spiros:
            # update
            spiro.update()
            # coumt completed spiros
            if spiro.drawingComplete:
                nComplete += 1
        # restart if all spiros are complete
        if nComplete == len(self.spiros):
            self.restart()
        # call the timer
        try:
            turtle.ontimer(self.update, self.deltaT)
        except:
            print("Exception, exiting.")
            exit(0)
            
    def toggleTurtles(self):
        """Uses built-in turtle methods to show/hide cursor. Faster when cursor hidden."""
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()

# standalone function, not part of any class 
def saveDrawing():
    # hide the turtle cursor
    turtle.hideturtle()
    # generate unique filenames
    dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    filename = 'spiro-' + dateStr
    print('saving drawing to {}.eps/png'.format(fileName))
    # get the tkinter canvas
    canvas = turtle.getcanvas()
    # save the canvas as a postscript image
    canvas.postscript(file = fileName + '.eps')
    # use the Pillow module to open the postscript(EPS) image file and convert to PNG
    img = Image.open(fileName + '.eps')
    img.save(fileName + '.png', 'png')
    # show the turtle cursor
    turtle.showturtle()
    
def main():
    
    # use Python's argparse module, create an ArgumentParser object to manage command line arguments
    parser = argparse.ArgumentParser(description='descStr')
    # add expected arguments
    parser.add_argument('--setparams', nargs=3, dest='sparams', required=False, help="The three arguments in sparams: R, r, l.")
    # parse args - makes the arguments available as properties of the args object
    # the values of the --sparams argument will be available through args.sparams
    args = parser.parse_args()
    
    # set the width of the drawing window to 80 percent of the screen width
    turtle.setup(width=0.8)
    # set the cursor shape to turtle
    turtle.shape('turtle')
    # set the title to Spirographs!
    turtle.title('Spirographs!')
    # add tghe key handler to save our drawings
    turtle.onkey(saveDrawing, "s")
    # start listening for user events
    turtle.listen()
    # hide the main turtle cursor
    turtle.hideturtle()
    
    # check for any arguments set to --sparams and draw the Spirograph
    if args.sparams:
        params = [float(x) for x in args.sparams]
        # draw the Spirograph with the given parameters
        col = (0.0, 0.0, 0.0)
        spiro = Spiro(0, 0, col, *params)
        spiro.draw()
    else:
        # create an animator object, this one will create 4 random spiros
        spiroAnim = SpiroAnimator(4)
        # add a key handler to toggle the turtle cursor
        turtle.onkey(spiroAnim.toggleTurtles, "t")
        # add a key handler to restart the animation
        turtle.onkey(spiroAnim.restart, "space")

    # start the turtle main loop
    turtle.mainloop()

# call main
if __name__ == '__main__':
    main()