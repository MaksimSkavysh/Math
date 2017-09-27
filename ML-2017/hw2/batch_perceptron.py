import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import round


def plot(samples, labels):
    length = len(samples);
    for i in range(0, length, 1):
        c = 'r' if labels[i] < 0 else 'b'
        plt.scatter(samples[i][0], samples[i][1], s=0.05, facecolors=c, edgecolors=c)
        # print('\rpl: %.2f' % (100 * i/length), end='')
        # sys.stdout.write("\033[F")
    plt.show()


def shuffle_samples_and_labels(samples, labels):
    rand = np.random.RandomState(1024)
    shuffle = rand.permutation(len(samples))
    samples, labels = samples[shuffle], labels[shuffle]
    return samples, labels


def multiply(a, b):
    return np.sum(np.multiply(a, b))


def perceptron(samples, labels):
    w = (0, 0)
    steps = 0
    length = len(samples)
    for i in range(0, length, 1):
        val = multiply(w, samples[i])
        # if np.sign(val) != labels[i]:
        if val <= 0:
            w = np.add(w, np.multiply(samples[i], labels[i]))
            steps += 1
    return w, steps


def calcualate_error(w, samples, labels):
    errors = 0
    length = len(samples)
    for i in range(0, length, 1):
        val = multiply(w, samples[i])
        if np.sign(val) != labels[i] and np.sign(val) != 0:
            errors = errors + 1
    return errors


N = 1000
P = 1000

min_x = -1.0
max_x = 1.0
min_y = -1.0
max_y = 1.0
bounds = (min_x, max_x, min_y, max_y)

x_N, y_N, x_P, y_P = round.generate(N, P, bounds)

samples = list(zip(x_N + x_P, y_N + y_P))
labels = [-1.0]*N + [1.0]*P
samples = np.array(samples)
labels = np.array(labels)
samples, labels = shuffle_samples_and_labels(samples, labels)

# plot(samples, labels)
# print(samples[0])
# print(samples[0][0], samples[0][1])

w, steps = perceptron(samples, labels)
print('steps: ', steps)
print('errors: ', calcualate_error(w, samples, labels))
