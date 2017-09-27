import numpy as np
import matplotlib.pyplot as plt
import math


def generate(N, P):

    min_x = 0.0
    max_x = 1.0
    min_y = 0.0
    max_y = 4.0

    R = (max_x - min_x) / 2
    R_y = (max_y - min_y) / 2

    center = (min_x + (max_x - min_x) / 2, min_y + (max_y - min_y) / 2)
    angle = np.random.random() * math.pi
    rad_min = angle
    rad_max = angle + math.pi

    radius = np.random.uniform(0, R, N)
    radius_y = np.random.uniform(0, R_y, N)
    radians = np.random.uniform(rad_min, rad_max, N)

    x_N = [0.0] * N
    y_N = [0.0] * N
    for i in range(0, N, 1):
        x_N[i] = radius[i] * math.cos(radians[i])
        y_N[i] = radius[i] * math.sin(radians[i])
    plt.scatter(x_N, y_N, s=0.05, facecolors='r', edgecolors='r')

    radius = np.random.uniform(0, R, P)
    radius_y = np.random.uniform(0, R_y, P)
    radians = np.random.uniform(rad_max, rad_max + math.pi, P)

    x_P = [0.0] * P
    y_P = [0.0] * P
    for i in range(0, P, 1):
        x_P[i] = radius[i] * math.cos(radians[i])
        y_P[i] = radius[i] * math.sin(radians[i])

    return x_N, y_N, x_P, y_P


def plot(x, y, c='r'):
    plt.scatter(x, y, s=0.05, facecolors=c, edgecolors=c)


def show():
    plt.show()


#
# N = 10000
# P = 5000

# generate(N, P)
