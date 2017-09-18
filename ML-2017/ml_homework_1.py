import numpy as np
import matplotlib.pyplot as plt


class Rect:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def check_dot(self, dot):
        (x, y) = dot
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2

    def update_bounds(self, dot):
        (x, y) = dot
        if self.x1 > x:
            self.x1 = x
        if self.x2 < x:
            self.x2 = x

        if self.y1 > y:
            self.y1 = y
        if self.y2 < y:
            self.y2 = y

    def plot(self, color='b'):
        plt.plot((self.x1, self.x2, self.x2, self.x1, self.x1), (self.y1, self.y1, self.y2, self.y2, self.y1), color=color)


def create_marks(S, square: Rect):
    marks = []
    print(len(S))
    for i in range(0, len(S), 1):
        mark = 1 if square.check_dot(S[i]) else 0
        marks.append(mark)
    return marks

m = 10
main_rect = Rect(0, 0, 1, 1)
q_side = 0.5 ** 0.5
q_rect = Rect(0, 0, q_side, q_side)

S = np.random.uniform(0, 1, (m, 2))
Y = create_marks(S, q_rect)
print(Y)


h_rect = Rect(1, 1, 0, 0)
for i in range(0, len(S), 1):
    if Y[i] == 1:
        h_rect.update_bounds(S[i])

main_rect.plot('black')
q_rect.plot('black')
h_rect.plot('r')
for i in range(0, len(S), 1):
    color = 'g' if Y[i] == 1 else 'r'
    plt.scatter(S[i, 0], S[i, 1], s=5, facecolors=color, edgecolors=color)
plt.show()
