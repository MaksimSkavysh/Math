import numpy as np
import matplotlib.pyplot as plt


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


def get_dot_on_line(k, b, x):
    return x, k*x + b


class Line:
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def get_dot(self, x):
        return get_dot_on_line(self.k, self.b, x)

N = 1000
P = 500

min_x = 0.0
max_x = 1.0
min_y = 0.0
max_y = 1.0

K = 0.5

x_arrays = np.random.uniform(min_x, max_x, P)

rect = Rect(min_x, max_x, min_y, max_y)
rect.plot()

plt.show()
