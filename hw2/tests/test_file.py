'''For testing the code'''

import hw2_debugging

def test_sorted_input():
    '''testing sorted input'''
    assert hw2_debugging.merge_sort([1,3,5,7]) == [1,3,5,7]

def test_reverse_sorted_input():
    '''testing reverse sorted input'''
    assert hw2_debugging.merge_sort([7,5,3,1]) == [1,3,5,7]

def test_general_input():
    '''testing general random array input'''
    assert hw2_debugging.merge_sort([4,2,1,3]) == [1,2,3,4]