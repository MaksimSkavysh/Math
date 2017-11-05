import random
import math
from math import exp
import numpy as np



def get_data(address):
    samples = []
    with open(address) as file:
        for line in file:
            parts = line.split(",")
            # last = parts[-1]
            # if last.strip() == currentIris:
            #     parts[-1] = 1
            # else:
            #     parts[-1] = 0
            samples.append([float(x) for x in parts])
    return samples


samples = get_data('./data/spambase.data.txt')
print(samples[0])