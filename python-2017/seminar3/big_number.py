from string import *
import re


def index(str_with_digits, args, k=5):
   result = []
   sum_of_occurrences = 0
   if type(args) == int:
       sum_of_occurrences = start_compute_occurrences(args, result, str_with_digits, sum_of_occurrences)
   else:
       for arg in args:
           sum_of_occurrences = start_compute_occurrences(arg, result, str_with_digits, sum_of_occurrences)
   return sum_of_occurrences, sorted(result)[:k]


def start_compute_occurrences(args, result, str_with_digits, sum_of_occurrences):
    start_index = 0
    str_digit, sum_of_occurrences = count_occurrences(args, str_with_digits, sum_of_occurrences)
    next_index = find(str_with_digits, str_digit, start_index)
    get_indexes_of_occurrences(next_index, result, str_digit, str_with_digits)
    return sum_of_occurrences


def get_indexes_of_occurrences(next_index, result, str_digit, str_with_digits):
    while next_index >= 0:
        start_index = next_index + 1
        result.append(start_index)
        next_index = find(str_with_digits, str_digit, start_index)


def count_occurrences(args, str_with_digits, sum_of_occurrences):
    str_digit = str(args)
    p = re.compile(str_digit)
    sum_of_occurrences += p.findall(str_with_digits).count(str_digit)
    return str_digit, sum_of_occurrences


print index("12345621322222", (2, 3, 56), 7)
