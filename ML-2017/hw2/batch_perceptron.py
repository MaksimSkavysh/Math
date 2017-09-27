import sys
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

def perceptron():
    w = (0, 0)

N = 2000
P = 1000

x_N, y_N, x_P, y_P = round.generate(N, P)

samples = list(zip(x_N + x_P, y_N + y_P))
labels = [-1.0]*N + [1.0]*P
samples = np.array(samples)
labels = np.array(labels)
samples, labels = shuffle_samples_and_labels(samples, labels)

plot(samples, labels)
print(samples[0])
print(samples[0][0], samples[0][1])
