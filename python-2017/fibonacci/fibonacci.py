def get_fibonacci_lower_than(maximum=1000):
    """get fibonacci numbers lower then maximum"""
    a, b = 0, 1
    fib_list = []
    while b < maximum:
        fib_list.append(a)
        a, b = b, a + b
    fib_list.append(a)
    return fib_list


def get_fibonacci(n):
    """get n fibonacci"""
    a, b = 0, 1
    fib_list = []
    while n:
        fib_list.append(a)
        a, b = b, a + b
        n = n - 1
    return fib_list


print(get_fibonacci(5))
