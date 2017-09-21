def add(x, y):
    return x + y


def calculate_special_sum(n):
    elements = [x*(x+1) for x in range(1, n, 1)]
    return reduce(add, elements)
