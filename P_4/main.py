## A program to implement a visual version of P_n in the plane

import turtle
import graph

## main function
def main():
    window = turtle.Screen()  # window to draw the shape

    element = graph.P4(window)

    window.onclick(element.animate)
    window.mainloop()

## call main function
main()