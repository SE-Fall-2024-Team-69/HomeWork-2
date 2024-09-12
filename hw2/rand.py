''' This is a docstring '''

#import random
import secrets

def random_array(arr):

    ''' Generates cryptographically strong random integers '''

    # shuffled_num = None

    # for enum_array in enumnerate(arr):
    #     arr[i] = random.randint(1,20)
    # return arr

    for enum_array in enumerate(arr):
        arr[enum_array[0]] = secrets.randbelow(20) + 1
    return arr
