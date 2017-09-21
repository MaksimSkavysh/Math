def is_pythagoras_triple((x, y, z)):
    return z * z == x * x + y * y


def get_triples_for_element(z):
    triples = [(x, int((z * z - x * x) ** 0.5), z) for x in range(1, z, 1)]
    triples = filter(is_pythagoras_triple, triples)
    return triples


def get_pythagoras_triples(n):
    z_elements = []
    for z in range(1, n + 1, 1):
        z_elements.extend(get_triples_for_element(z))
    return z_elements

print get_pythagoras_triples(10)
