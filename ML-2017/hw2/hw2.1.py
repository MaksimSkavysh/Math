import numpy as np
import matplotlib.pyplot as plt
import math


class Rect:
    def __init__(self, min_x=0.0, max_x=0.0, min_y=0.0, max_y=0.0):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.square = self.calculate_square()

    def check_dot(self, dot):
        (x, y) = dot
        return self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y

    def plot(self, color='b'):
        plt.plot((self.min_x, self.max_x, self.max_x, self.min_x, self.min_x),
                 (self.min_y, self.min_y, self.max_y, self.max_y, self.min_y),
                 color=color)

    def calculate_square(self):
        if self.max_x <= self.min_x or self.max_y <= self.min_y:
            return 0
        self.square = (self.max_x - self.min_x) * (self.max_y - self.min_y)
        return self.square


def get_y(x, b, w1, w2, rect, default):
    val = (-b - w1 * x) / w2
    if rect.min_y <= val <= rect.max_y:
        return val
    # if rect.min_y > val:
    #     return rect.min_y
    # if rect.max_y < val:
    #     return rect.max_y
    return default


def get_x(y, b, w1, w2):
    return (-b - w2 * y) / w1


def get_value(params, x, y):
    (w1, w2, b) = params
    return w1 * x + w2 * y + b


def get_x_bounds(params, rect):
    (w1, w2, b) = params
    x_bounds = list()
    x_bounds.append(rect.min_x)
    x_bounds.append(rect.max_x)
    if w1 != 0:
        x_0 = get_x(rect.min_y, b, w1, w2)
        x_1 = get_x(rect.max_y, b, w1, w2)
        if rect.min_x <= x_0 <= rect.max_x:
            x_bounds.append(x_0)
        if rect.min_x <= x_1 <= rect.max_x:
            x_bounds.append(x_1)
    x_bounds.sort()
    right_bounds = [x_bounds[1], x_bounds[-1]]
    left_bounds = [x_bounds[0], x_bounds[2]]
    print(x_bounds[1:3])
    return right_bounds, left_bounds


def find_value_extr(params, rect):
    (w1, w2, b) = params
    corners_value = list()
    corners_value.append(get_value(params, rect.min_x, rect.min_y))
    corners_value.append(get_value(params, rect.min_x, rect.max_y))
    corners_value.append(get_value(params, rect.max_x, rect.min_y))
    corners_value.append(get_value(params, rect.max_x, rect.max_y))
    return min(corners_value), max(corners_value)


# def generate(params, rect, P):
#     (w1, w2, b) = params
#
#     x_bounds = get_x_bounds((w1, w2, b_divide), rect)
#
#     x_P = np.random.uniform(x_bounds[0], x_bounds[1], P)
#     y_P = [0.0] * P
#     for i in range(0, P, 1):
#         y_P[i] = get_y(x_P[i], b, w1, w2)
#         y_P[i] = rect.max_y - np.random.random() * (rect.max_y - y_P[i])
#     plt.scatter(x_P, y_P, s=0.05, facecolors='r', edgecolors='r')
#     return x_P, y_P


N = 10000
P = 5000

w = [-2, 1]
w1, w2 = w

min_x = 0.0
max_x = 1.0
min_y = 0.0
max_y = 1.0

rect = Rect(min_x, max_x, min_y, max_y)
rect.plot()

b1 = -(w1 * min_x + w2 * min_y)
b2 = -(w1 * max_x + w2 * max_y)
b3 = -(w1 * max_x + w2 * min_y)
b4 = -(w1 * min_x + w2 * max_y)
b_min = min(b1, b2, b3, b4)
b_max = max(b1, b2, b3, b4)
# b_divide = np.random.random()*(b2 - b1)
b_divide = (b2 - b1) / 2


# f_min, f_max = find_value_extr((w1, w2, b_divide), rect)
# values_N = np.random.uniform(f_min, 0, N)
right_bounds, left_bounds = get_x_bounds((w1, w2, b_divide), rect)

# default = rect.max_y if w1*w2 < 0 else rect.min_y
default = rect.max_y
x_N = np.random.uniform(right_bounds[0], right_bounds[1], N)
y_N = [0.0] * N
for i in range(0, N, 1):
    y_N[i] = get_y(x_N[i], b_divide, w1, w2, rect, default)
    y_N[i] = rect.min_y + np.random.random()*(y_N[i] - rect.min_y)
plt.scatter(x_N, y_N, s=0.05, facecolors='b', edgecolors='b')


# default = rect.max_y if w1*w2 > 0 else rect.min_y
default = rect.min_y
x_P = np.random.uniform(left_bounds[0], left_bounds[1], P)
y_P = [0.0] * P
for i in range(0, P, 1):
    y_P[i] = get_y(x_P[i], b_divide, w1, w2, rect, default)
    y_P[i] = rect.max_y - np.random.random()*(rect.max_y - y_P[i])
plt.scatter(x_P, y_P, s=0.05, facecolors='r', edgecolors='r')

plt.show()
