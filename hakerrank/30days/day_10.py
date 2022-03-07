
import math
import os
import random
import re
import sys


def get_valid_int(number):
    if 1 <= number <= 1000000:
        return number
    return 1


def get_binary(number):
    if number == 1:
        return "1"
    return f"{number % 2}{get_binary(number // 2)}"


if __name__ == '__main__':
    n = int(input().strip())
    n = get_valid_int(n)
    bn = get_binary(n)[::-1]
    consequent_ones = [1, ]
    consequent_ones_index = 0
    for i in range(1, len(bn)):
        if bn[i] == "1":
            consequent_ones[consequent_ones_index] += 1
        else:
            consequent_ones.append(0)
            consequent_ones_index += 1

    print(max(consequent_ones))

