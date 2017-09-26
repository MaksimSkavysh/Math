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


def get_y(x, b, w1, w2):
    return (-b - w1*x) / w2


def get_x(y, b, w1, w2):
    return (-b - w2*y) / w1


def generate_points(b_min, b_divide, w, rect):
    # x_lower = get_x(rect.min_y, b_divide, w[0], w[1])
    # x_upper = get_x(rect.max_y, b_divide, w[0], w[1])
    # if x_lower < x_upper:
    #     x_min = max(x_lower, rect.min_x)
    #     x_max = min(x_upper, rect.max_x)
    # else:
    #     x_min = max(x_upper, rect.min_x)
    #     # x_max = min(x_lower, rect.max_x)
    #     x_max = rect.max_x if rect.max_x > x_lower else x_lower
    # plt.scatter([x_min, x_max], [0, 0], s=155.5, facecolors='g', edgecolors='g')
    # x_array = np.random.uniform(x_min, x_max, N)

    b_array = np.random.uniform(b_min, b_divide, N)
    y_array = [0.0]*N
    x_array = [0.0]*N
    for i in range(0, N, 1):
        x_lower = get_x(rect.min_y, b_divide, w[0], w[1])
        x_upper = get_x(rect.max_y, b_divide, w[0], w[1])
        if x_lower < x_upper:
            x_min = max(x_lower, rect.min_x)
            x_max = min(x_upper, rect.max_x)
        else:
            x_min = max(x_upper, rect.min_x)
            # x_max = min(x_lower, rect.max_x)
            x_max = rect.max_x if rect.max_x > x_lower else x_lower
        x_element = np.random.random()*(x_max - x_min)

        y_array[i] = x_element
        y_array[i] = get_y(x_element, b_array[i], w[0], w[1])

    plt.scatter(x_array, y_array, s=0.5, facecolors='g', edgecolors='g')



N = 1000
P = 500

w = [2, 1]

min_x = 0.0
max_x = 1.0
min_y = 0.0
max_y = 1.0

rect = Rect(min_x, max_x, min_y, max_y)
rect.plot()

b1 = -(w[0]*min_x + w[1]*min_y)
b2 = -(w[0]*max_x + w[1]*max_y)
b3 = -(w[0]*max_x + w[1]*min_y)
b4 = -(w[0]*min_x + w[1]*max_y)
b_min = min(b1, b2, b3, b4)
b_max = max(b1, b2, b3, b4)
b_divide = np.random.random()*(b2 - b1)

generate_points(b_min, b_divide, w, rect)

# x = np.random.uniform(min_x, max_x, N)
# # y = np.random.uniform(min_y, max_y, N)
# y = list(map(lambda x: get_y(x, b_min, w[0], w[1]), x))
# plt.scatter(x, y, s=0.05, facecolors='b', edgecolors='b')
#
#
# x = np.random.uniform(min_x, max_x, N)
# y = list(map(lambda x: get_y(x, b_max, w[0], w[1]), x))
# plt.scatter(x, y, s=0.05, facecolors='r', edgecolors='r')

x = np.random.uniform(min_x, max_x, N)
y = list(map(lambda x: get_y(x, b_divide, w[0], w[1]), x))
plt.scatter(x, y, s=0.05, facecolors='g', edgecolors='g')


plt.show()



def generate_points(b_min, b_divide, w, rect):
    # x_lower = get_x(rect.min_y, b_divide, w[0], w[1])
    # x_upper = get_x(rect.max_y, b_divide, w[0], w[1])
    # if x_lower < x_upper:
    #     x_min = max(x_lower, rect.min_x)
    #     x_max = min(x_upper, rect.max_x)
    # else:
    #     x_min = max(x_upper, rect.min_x)
    #     # x_max = min(x_lower, rect.max_x)
    #     x_max = rect.max_x if rect.max_x > x_lower else x_lower
    # plt.scatter([x_min, x_max], [0, 0], s=155.5, facecolors='g', edgecolors='g')
    # x_array = np.random.uniform(x_min, x_max, N)

    b_array = np.random.uniform(b_min, b_divide, N)
    y_array = [0.0]*N
    x_array = [0.0]*N
    for i in range(0, N, 1):
        x_lower = get_x(rect.min_y, b_divide, w[0], w[1])
        x_upper = get_x(rect.max_y, b_divide, w[0], w[1])
        if x_lower < x_upper:
            x_min = max(x_lower, rect.min_x)
            x_max = min(x_upper, rect.max_x)
        else:
            x_min = max(x_upper, rect.min_x)
            # x_max = min(x_lower, rect.max_x)
            x_max = rect.max_x if rect.max_x > x_lower else x_lower
        x_element = np.random.random()*(x_max - x_min)

        y_array[i] = x_element
        y_array[i] = get_y(x_element, b_array[i], w[0], w[1])

    plt.scatter(x_array, y_array, s=0.5, facecolors='g', edgecolors='g')
