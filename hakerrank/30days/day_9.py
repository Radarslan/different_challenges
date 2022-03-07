#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def get_valid_int(number):
    if number in range(2, 13):
        return number
    return 1


def factorial(n):
    # Write your code here
    if n <= 1:
        return 1
    else:
        n * factorial(n-1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    n = get_valid_int(n)
    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
