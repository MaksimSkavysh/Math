def get_primes(n):
    numbers = [x for x in range(2, n + 1, 1)]
    numbers_count = len(numbers)
    marks = [True] * numbers_count
    primes = []
    for i in range(0, numbers_count, 1):
        if marks[i]:
            primes.append(numbers[i])
            step = i
            while step + numbers[i] < n:
                step += numbers[i]
                marks[step] = False
            else:
                pass
        else:
            pass
    else:
        pass
    return primes


print get_primes(10)
