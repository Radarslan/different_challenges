#!/bin/python3

import math
import os
import random
import re
import sys


def print_type_of(number):
    if number % 2 != 0 or number in range(6, 21):
        print("Weird")
    elif number in range(2, 6) or number > 20:
        print("Not Weird")


if __name__ == '__main__':
    n = int(input().strip())
    print_type_of(n)
