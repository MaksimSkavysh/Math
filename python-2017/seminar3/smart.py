def smart_function_generator():
    counter = [0]

    def inner_function():
        counter[0] = counter[0] + 1
        return counter[0]

    return inner_function

smart_function = smart_function_generator()

