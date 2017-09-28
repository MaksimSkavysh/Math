import numpy as np
import matplotlib.pyplot as plt
import math


def generate(N, P, bounds, R_mult=0, angle_min=0):
    min_x, max_x, min_y, max_y = bounds

    R = min((max_x - min_x) / 2, (max_y - min_y) / 2)
    center = ((max_x + min_x) / 2, (max_y - min_y) / 2)
    R_min = R*R_mult

    angle = np.random.random() * math.pi
    rad_min = angle
    rad_max = angle + math.pi

    radius = np.random.uniform(R_min, R, N)
    radians = np.random.uniform(rad_min + angle_min, rad_max - angle_min, N)
    x_N = [0.0] * N
    y_N = [0.0] * N
    for i in range(0, N, 1):
        x_N[i] = center[0] + radius[i] * math.cos(radians[i])
        y_N[i] = center[1] + radius[i] * math.sin(radians[i])

    radius = np.random.uniform(R_min, R, P)
    radians = np.random.uniform(rad_max + angle_min, rad_max + math.pi - angle_min, P)
    x_P = [0.0] * P
    y_P = [0.0] * P
    for i in range(0, P, 1):
        x_P[i] = center[0] + radius[i] * math.cos(radians[i])
        y_P[i] = center[1] + radius[i] * math.sin(radians[i])

    return x_N, y_N, x_P, y_P


def plot(x, y, c='r'):
    plt.scatter(x, y, s=0.05, facecolors=c, edgecolors=c)


def show():
    plt.show()


#
# N = 10000
# P = 5000

# generate(N, P)
