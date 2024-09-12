''' This is a docstring '''

import secrets

def random_array(arr):

    ''' Generates cryptographically strong random integers '''

    for enum_array in enumerate(arr):
        arr[enum_array[0]] = secrets.randbelow(20) + 1
    return arr
