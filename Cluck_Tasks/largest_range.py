"""
Write a function that takes in an array of integers
and returns an array of length 2 representing the largest range of numbers contained in an array.
The first number in the output array should be the first number in the range while the
second number should be the last number in the range. A range of numbers is defined as a set of
numbers that come right after each other in the set of real integers. For instance, the output array
[2,6] represents the range [2, 3, 4, 5, 6] which is a range of length 5. Note that numbers do not need to be
ordered or adjacent in the array in order to form a range. Assume that there will only be one largest range.


Sample input: [4, 11, 3, 0, 1, 15, 5, 2, 10, 7, 12, 6]
Sample output: [0, 7]
"""
from random import randint
from time import time


def largest_range_no_sort(array):
    """
    OPTIMAL SOLUTION
    """
    right = left = 0
    hash_table = {key: 0 for key in array}

    for number in array:
        print(hash_table)
        if hash_table[number] == 0:
            right_count = number + 1
            left_count = number - 1

            while left_count in hash_table:
                hash_table[left_count] = 1
                left_count -= 1
            left_count += 1

            while right_count in hash_table:
                hash_table[right_count] = 1
                right_count += 1
            right_count -= 1

            if (right - left) <= (right_count - left_count):
                right = right_count
                left = left_count

    return [left, right]


l = [1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14]

started = time()
res = largest_range_no_sort(l)
elapsed = time() - started

print(f'\nQueue time elapsed: {elapsed:.2f}s')
print(res)
