def set_bit(number, k):
    print 'initial:', bin(number)
    mask = 1 << k
    print 'mask:', bin(mask)
    number |= mask
    print 'result:', bin(number)
    return number


def clear_bit(number, k):
    print 'initial:', bin(number)
    mask = ~ (1 << k)
    print 'mask:', bin(mask)
    number &= mask
    print 'result:', bin(number)
    return number


def test_bit(number, k):
    print 'initial:', bin(number)
    mask = 1 << k
    print 'mask:', bin(mask)
    number = mask & number
    print 'result:', bool(number)
    return bool(number)


set_bit(5, 1)
clear_bit(6, 1)
test_bit(6, 1)
test_bit(5, 1)
