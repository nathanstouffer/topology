"""This is a class to visualize the graph P4.
    Each element of P4 is uniquely defined by to angles: theta and phi."""

import turtle
import point

class P4:
    # global variables
    dist = 150
    moving = False

    """Cosntructor to initialize the image of an elemnt of P_4"""
    def __init__(self, window):
        self.window = window
        points = self.initializeGraph()
        self.ptheta = points[0]
        self.pphi = points[1]

    """Method to begin animation if not already started"""
    def animate(self, x, y):
        if (self.moving == False):
            self.moving = True
            self.traverse()

    """Method to make a traversal through the graph of P_4 and display
    the four points in each state"""
    def traverse(self):
        # traverse through the graph of P_4
        for angle in range(0, 180):
            self.ptheta.incrementAngle()
            self.pphi.incrementAngle()
        for angle in range(0, 360):
            self.pphi.incrementAngle()
        for angle in range(0, 180):
            self.ptheta.incrementAngle()
            self.pphi.incrementAngle()
        for angle in range(0, 360):
            self.ptheta.incrementAngle()
        # set moving to False after traversal
        self.moving = False

    """Method to initialize the points on the graph of P_4"""
    def initializeGraph(self):
        # variables to represent the origin
        origin = turtle.Turtle()
        self.initializeTurtle(origin)
        origin.color([0, 0, 0])
        origin.setpos(0, 0)

        # variable to represent the complex number 1
        one = turtle.Turtle()
        self.initializeTurtle(one)
        one.color([0, 0, 0])
        one.setpos(self.dist, 0)

        # return a list of the two points
        return [point.Point(self.window, [1, 0], 0, self.dist),
                point.Point(self.window, [0, 0], 0, self.dist)]

    """Method to initialize a turtle with appropriate attributes"""
    def initializeTurtle(self, turt):
        turt.shape("circle")
        turt.shapesize(0.9, 0.9)
        turt.up()
        turt.speed(0)
