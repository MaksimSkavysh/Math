def concat_parts(left_part, right_part):
    lst = []
    while left_part and right_part:
        if left_part[0] < right_part[0]:
            lst.append(left_part.pop(0))
        else:
            lst.append(right_part.pop(0))
    lst.extend(left_part + right_part)
    return lst


def process_sorting(array):
    length = len(array)
    if length == 1:
        return array
    left_part = process_sorting(array[:length / 2])
    right_part = process_sorting(array[length / 2:])
    return concat_parts(left_part, right_part)


def sort(array):
    is_tuple = type(array) is tuple
    sorted_array = process_sorting(list(array))
    return tuple(sorted_array) if is_tuple else sorted_array


print sort((1, 2, 3, 4, 1, 2))
