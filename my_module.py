
test = 'Test String'


def find_index(search_in, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(search_in):
        if value == target:
            return i

    return - 1


if __name__ != "__main__":
    print('Importing my_module')
