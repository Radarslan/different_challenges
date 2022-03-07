#!/bin/python3

import math
import os
import random
import re
import sys

import cProfile, pstats, io
import functools
import re
import timeit
import functools

from datetime import datetime
from functools import lru_cache
from itertools import combinations
from math import comb
from string import ascii_uppercase as alphabet
from random import randint

import re

from itertools import combinations, islice


def profile(fnc):
    """A decorator that uses cProfile to profile a function"""

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner


#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#
def bitwiseAnd(N, K):
    maximum = 0
    j = K-1
    for i in range(N, 2, -1):
        if i == j:
            continue
        result = i & j
        if result > maximum:
            maximum = result
    return maximum


# Write your code here

# def do_the_work(test):
#     n, k = test
#     n = int(n)
#     k = int(k)
#     return bitwiseAnd(n, k)
# print(f"{minus_line} {n}, {k}")
# cProfile.run('bitwiseAnd(n, k)')
# print(lines)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # t = int(input().strip())
    #
    # for t_itr in range(t):
    #     first_multiple_input = input().rstrip().split()
    #
    #     count = int(first_multiple_input[0])
    #
    #     lim = int(first_multiple_input[1])
    #
    #     res = bitwiseAnd(count, lim)
    #
    #     fptr.write(str(res) + '\n')
    #
    # fptr.close()
    start = datetime.utcnow()
    print(start)
    tests = []

    file_name = "input.txt"
    with open(file_name, "r") as file:
        number_of_tests = int(file.readline().strip())
        tests = [file.readline().split() for i in range(number_of_tests)]

    lines = "\n" * 3
    minus_line = "-" * 75
    for test in tests:
        n, k = test
        n = int(n)
        k = int(k)
        print(bitwiseAnd(n, k))
    # for test in tests:
    #     n, k = test.split()
    #     n = int(n)
    #     k = int(k)
    #     print(f"{minus_line} {n}, {k}")
    #     cProfile.run('bitwiseAnd(n, k)')
    #     print(lines)

    end = datetime.utcnow()
    print(end)
    print(end - start)
