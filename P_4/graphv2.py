# class to represent an element of P_n

import turtle
import math
import random


class Element:
    # global variables
    n = 0  # number of points to compute
    dist = 150  # distance between points
    points = []  # points that compose P_n

    moving = False
    angle_step = 1
    error_margin = 0.01

    # constructor to create initial graph
    def __init__(self, window, n):
        self.window = window
        self.n = n

        self.initializeGraph()

        # mapper turtle to find the location of initial vertices
        mapper = turtle.Turtle()
        mapper.hideturtle()
        self.initializeTurtle(mapper)

        # send mapper to complex number 1
        mapper.setpos(self.dist, 0)

        # determine the angle between sides
        angle = 360 / n
        for i in range(0, n - 2):
            mapper.left(angle)
            mapper.forward(self.dist)
            v = turtle.Turtle()
            self.initializeTurtle(v)
            v.setpos(mapper.pos())
            self.points.append(v)

    def animate(self, x, y):
        if (self.moving == False):
            self.moving = True
            # print("starting animation")
            self.tick(2)
        else:
            # print("ending animation")
            self.moving = False

    def tick(self, index):
        if (self.moving == True):
            if (index < self.n):
                # assume curr is the (n-1) point
                curr = self.points[index]

                # set theta to radians
                theta = math.radians(self.angle_step)

                # iterate around circle
                for angle in range(0, 361):
                    # recursive call
                    self.tick(index + 1)
                    # identify prev and next
                    prev = self.points[0]
                    # change prev if curr is not (n-1) point
                    if (index < self.n - 1):
                        prev = self.points[index - 1]
                    # compute phi
                    phi = self.computePhi(curr, prev)
                    # compute new position
                    newx = self.dist * math.sin(phi + theta)  # trig function is like so since phi is measured of y-axis
                    newy = self.dist * math.cos(phi + theta)
                    prevpos = prev.pos()
                    newpos = prevpos + [newx, newy]
                    if (self.moving == True):
                        valid = self.checkValid(curr, prev)
                        if (index == self.n - 1):
                            valid = self.checkValid(curr, self.points[self.n - 2])
                        if (valid == True):
                            curr.setpos(newpos)


    # function to return phi, the angle the point off the y-axis
    def computePhi(self, curr, prev):
        # compute direction vector
        vec = curr.pos() - prev.pos()
        # dot vector with j-hat leaves only y component
        vecy = vec[1]
        # magnitude of vector
        vec_mag = math.sqrt(math.pow(vec[0], 2) + math.pow(vec[1], 2))
        phi = math.acos(vecy / vec_mag)
        # check quadrant
        if (vec[0] < 0):
            phi = 2 * math.pi - phi
        return phi

    def checkValid(self, curr, prev):
        # compute distances
        dist1 = self.computeDist(curr, prev)
        # print(dist1, dist2)
        # compute error margin
        margin = [self.dist - self.error_margin, self.dist + self.error_margin]
        # return false if distance is outside margin
        if (dist1 < margin[0] or dist1 > margin[1]):
            return False
        # otherwise return true
        return True

    def computeDist(self, p1, p2):
        # get coordinates
        p1pos = p1.pos()
        p2pos = p2.pos()
        # compute differences
        diffx = p2pos[0] - p1pos[0]
        diffy = p2pos[1] - p1pos[1]
        # compute distance
        dist = math.sqrt(math.pow(diffx, 2) + math.pow(diffy, 2))
        return dist

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

        self.points.append(origin)
        self.points.append(one)

    def initializeTurtle(self, turt):
        turt.shape("circle")
        turt.shapesize(0.9, 0.9)
        rand_color = self.chooseColor()
        turt.color(rand_color)
        turt.up()
        turt.speed(0)

    def chooseColor(self):
        red = random.random()
        green = random.random()
        blue = random.random()
        return [red, green, blue]