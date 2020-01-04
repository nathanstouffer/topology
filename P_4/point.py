""""A python file containing a class that represents a point.
    Each point has an anchor (a point in the complex plane) and
    an angle theta off the horizontal. In addition, there are
    """

import random
import turtle
import math

class Point:

    """Constructor to initialize a point in an element of P_4
        anchor is a complex number in the form of a list,
        theta is an angle (measurea in degrees), and
        radius is a distance from the anchor"""
    def __init__(self, window, anchor, theta, radius):
        self.window = window
        self.theta = theta
        self.radius = radius
        self.anchor_real = anchor[0] * self.radius
        self.anchor_imag = anchor[1] * self.radius

        # initialize point at correct location
        p = turtle.Turtle()
        self.initializeTurtle(p)
        p.setpos(self.anchor_real, self.anchor_imag)
        p.left(theta)
        p.forward(self.radius)
        self.point = p

    """Method to increment the angle (theta) off the horizontal"""
    def incrementAngle(self):
        # change angle
        self.theta += 1
        self.theta = self.theta % 360

        # update position
        rad = math.radians(self.theta)
        # compute (x,y) coordinates from anchor
        x = self.radius * math.cos(rad)
        y = self.radius * math.sin(rad)
        # set position
        self.point.setpos(self.anchor_real + x,
                          self.anchor_imag + y)

    """Method to initialize a turtle with appropriate attributes"""
    def initializeTurtle(self, turt):
        turt.shape("circle")
        turt.shapesize(0.9, 0.9)
        rand_color = self.randColor()
        turt.color(rand_color)
        turt.up()
        turt.speed(0)

    """Method to set the color of the point to a random value"""
    def randColor(self):
        red = random.random()
        green = random.random()
        blue = random.random()
        return [red, green, blue]