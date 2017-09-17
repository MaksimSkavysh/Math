def numeral_sum(number):
    result = 0
    while number:
        result += number % 10
        number = number // 10
    return result


def split_number(number):
    first_half = number // 1000
    second_half = number % 1000
    return first_half, second_half


def check_ticket(number):
    print number
    first_half, second_half = split_number(number)
    first_sum = numeral_sum(first_half)
    second_sum = numeral_sum(second_half)
    return first_sum == second_sum


def is_lucky_ticket(number):
    i = 1
    while not check_ticket(number):
        number += ((-1) ** i) * i
        i = i + 1
    return number


print is_lucky_ticket(100999)
