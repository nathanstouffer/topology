# class to represent an element of P_n

import turtle
import math
import random


class Element:
    # global variables
    n = 0  # number of points to compute
    dist = 150  # distance between points
    points = []  # points that compose P_n

    world_ref = [0, 0]  # reference for converting between world and turtle screen
    screen_ref = [0, 0]  # reference for converting between world and turtle screen

    selected_index = -1  # index of selected point
    selection = None  # the selected point

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
        self.rotatePoint(x, y)

    def rotatePoint(self, x, y):
        # print(x, y)
        self.selectPoint(x, y)
        mouse = turtle.Turtle()
        mouse.hideturtle()
        self.initializeTurtle(mouse)

        while (self.selected_index != -1):
            # print("change mouse position") # testing purposes
            worldx = mouse.screen.cv.winfo_pointerx()
            worldy = mouse.screen.cv.winfo_pointery()
            mouse_coord = self.convertToScreenCoord([worldx, worldy])
            # print(mouse_coord)  # testing purposes

            new_pos = self.computeValidPoint(mouse_coord[0], mouse_coord[1])
            if (self.selected_index != -1):
                pos = self.selection.pos()

                # compute differences
                diffx = new_pos[0] - pos[0]
                diffy = new_pos[1] - pos[1]

                other = self.points[2]
                other_pos = other.pos()
                other_pos = [other_pos[0] + diffx, other_pos[1] + diffy]

                # adjust points
                self.selection.setpos(new_pos)
                self.points[2].setpos(other_pos)  # change to be general

    def selectPoint(self, x, y):
        new_selected_index = self.pointClickedIndex(x, y)
        # test if point is currently selected
        if (self.selected_index == -1):
            # test current click selects a point
            if (new_selected_index != -1):
                print("selected: " + str(new_selected_index + 1))
                self.selected_index = new_selected_index
                self.selection = self.points[self.selected_index]
        # this means a point is currently selected
        else:
            # if current click does not click a point
            if (new_selected_index == -1):
                print("selected: none")
                self.selected_index = -1
                self.selection = None
            # if current click selects current point
            elif (new_selected_index == self.selected_index):
                print("selected: none")
                self.selected_index = -1
                self.selection = None
            else:
                print("selected: " + str(new_selected_index + 1))
                self.selected_index = new_selected_index
                self.selection = self.points[new_selected_index]

    def computeValidPoint(self, mousex, mousey):
        curr = self.selected_index

        if (curr + 1 == self.n):
            dist_sqrd = math.pow(mousex, 2) + math.pow(mousey, 2)
            if (dist_sqrd != 0):
                const = math.sqrt(math.pow(self.dist, 2) / dist_sqrd)
                # print(const) # testing purposes
                return [const * mousex, const * mousey]
            else:
                return [mousex, mousey]

    # function to return the index of the point that is clicked
    def pointClickedIndex(self, x, y):
        for i in range(2, len(self.points)):
            point = self.points[i]
            point_pos = point.pos()

            dist = math.pow(point_pos[0] - x, 2) + math.pow(point_pos[1] - y, 2)

            if (dist < 100):
                self.setReferences(x, y)
                return i
        return -1

    # function to take in a click in world coordinates and
    # convert to screen coordinates
    def convertToScreenCoord(self, world_coord):
        # set the differences in x and y
        xdiff = world_coord[0] - self.world_ref[0]
        ydiff = self.world_ref[1] - world_coord[1]  # world is measured from top-left of screen

        # converted coordinates
        screen_coord = [self.screen_ref[0] + xdiff, self.screen_ref[1] + ydiff]
        return screen_coord

    # method to set the values in the reference lists
    def setReferences(self, screenx, screeny):
        # set screen reference point
        self.screen_ref = [screenx, screeny]

        # create turtle to follow mouse
        mouse = turtle.Turtle()
        mouse.hideturtle()
        self.initializeTurtle(mouse)

        # set world reference point
        worldx = mouse.screen.cv.winfo_pointerx()
        worldy = mouse.screen.cv.winfo_pointery()
        self.world_ref = [worldx, worldy]

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
