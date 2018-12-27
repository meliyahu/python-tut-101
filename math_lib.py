
def square(a):
    return a * a


def multiply(a, b):
    ''' Multipy function '''
    return a * b


def add(a, b):
    '''Addition function'''
    return a + b


def subtract(a, b):
    '''Subration function'''
    return a - b


def divide(a, b):
    '''Division function'''
    if (b == 0):
        raise ValueError('Cannot divide by zero!')
    return a / b
