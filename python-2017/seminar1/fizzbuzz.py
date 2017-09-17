for i in range(2, 51, 2):
    if not i % 3 and not i % 5:
        print 'FizzBazz'
    elif not i % 3:
        print 'Fizz'
    elif not i % 5:
        print 'Bazz'
    else:
        print i
