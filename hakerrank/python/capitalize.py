#!/bin/python3

import math
import os
import random
import re
import sys


def get_valid_string(string):
    string = string[:1000] if s else ""
    return re.sub("[^a-zA-Z0-9 ]+", "", string).strip()


def solve(s):
    s = get_valid_string(s)
    new_string = ""
    if s:
        last_index = 0
        new_string = s[0].upper()
        for index in range(1, len(s)):
            onw = s[index]
            if s[index].isalnum() and (re.search("\s+", s[index-1])):
                new_string += s[last_index+1:index] + s[index].upper()
                last_index = index
        new_string += s[last_index+1:index+1]
    return new_string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    print(s)
    result = solve(s)
    print(result)
    # fptr.write(result + '\n')
    #
    # fptr.close()
