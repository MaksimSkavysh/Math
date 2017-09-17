import numpy as np
import matplotlib.pyplot as plt


class RectHypotise:
    def __init__(self, a1, b1, a2, b2):
        self.a1 = 0
        self.b1 = 0
        self.a2 = 0
        self.b2 = 0

    def train(self, samples, labels):
        for i in range(0, labels.length+1):
            self.a1 = 1

    def check(self, x1, x2):
        return self.a1 <= x1 <= self.b1 and self.a2 <= x2 <= self.b2


m = 100

S = np.random.uniform(0, 1, (m, 2))
Y = np.random.randint(0, 2, m)
print(Y)

plt.scatter(S[:, 0], S[:, 1], s=5, facecolors='b', edgecolors='b')
plt.show()
