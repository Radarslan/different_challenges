#!/bin/python3

import math
import os
import random
import re
import sys


def get_valid_int(number, min, max):
    if min <= number <= max:
        return number
    return min


def get_number_of_sorts_in_bubble_sort(array):
    number_of_swaps = 0
    for i in range(len(array)):
        for j in range(n-1):
            if array[j] > a[j+1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                number_of_swaps += 1
        if number_of_swaps == 0:
            break
    return number_of_swaps


if __name__ == '__main__':
    n = int(input().strip())
    n = get_valid_int(n, 2, 600)
    a = list(map(int, input().rstrip().split()))
    for number in a:
        number = get_valid_int(number, 1, 10 ** 6 * 2)

    # Write your code here

    number_of_swaps = get_number_of_sorts_in_bubble_sort(a)
    print(f"Array is sorted in {number_of_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
