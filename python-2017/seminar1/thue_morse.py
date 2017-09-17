def get_sequence_item(k):
    if k == 0:
        return 1
    number = 0
    for i in range(1, k + 1):
        print(bin(number))
        mask = ~number
        print(bin(mask))
        number = number << i
        number = number + mask
        print(bin(number))
        print('--------')

    return None


get_sequence_item(2)
