#!/bin/python3

import math
import os
import random
import re
import sys


def get_valid_int(number, min, max):
    if min <= number <= max:
        return number
    return max


if __name__ == '__main__':
    N = int(input().strip())
    N = get_valid_int(N, 2, 30)
    names = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        emailID = first_multiple_input[1]
        if re.search(r"@gmail.com", emailID):
            names.append(first_multiple_input[0])

    for name in sorted(names):
        print(name)

