import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d as plt3
import math

def main():
    mult2d = math.pi / 200    # multiple for functions

    # lists for values
    x2val = []
    y2val = []

    # populate 2-d points
    for p in range(0, 400):
        x2val.append(100 * math.cos(mult2d * p))
        y2val.append(100 * math.sin(mult2d * p))

    # create 3-d data set
    x3val = []
    y3val = []
    z3val = []

    mult3d = math.pi / 20

    # populate 3- points
    for p in range(0, 40):
        for q in range(0, 20):
            x3val.append(math.cos(mult3d*p)*math.sin(mult3d*q))
            y3val.append(math.sin(mult3d*p)*math.sin(mult3d*q))
            z3val.append(math.cos(mult3d*q))

    # plot samples
    plt.figure(1)
    plt.scatter(x2val, y2val)
    plt.title("2-d sample")

    plt.figure(2)
    ax = plt.axes(projection='3d')
    ax.scatter3D(x3val, y3val, z3val)
    plt.title("3-d sample")

    plt.show()

main()
