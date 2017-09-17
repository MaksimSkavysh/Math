def set_bit(number, k):
    mask = 1 << k
    return number | mask


def clear_bit(number, k):
    mask = ~ (1 << k)
    return number & mask


def test_bit(number, k):
    mask = 1 << k
    return bool(mask & number)
