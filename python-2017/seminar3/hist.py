def distribute(samples, n):
    max_sample, min_sample = max(samples),  min(samples)
    h = (max_sample - min_sample) / n

    samples = sorted(samples)
    curstep_min = min_sample
    curstep_max = curstep_min + h
    
    i = 0
    counter = 0
    result = []

    while i < len(samples):
        if curstep_min <= samples[i] <= curstep_max:
            counter = counter + 1
            i = i + 1
        else:
            result.append(counter)
            counter = 0
            curstep_min = curstep_max
            curstep_max = curstep_max + h
    result.append(counter)
    return result
