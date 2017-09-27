def get_unique(sequence):
    pairs = dict(zip(sequence, [0]*len(sequence)))
    for x in sequence:
        pairs[x] += 1
    return pairs.items()

print get_unique([1, 2, 1, 3])
