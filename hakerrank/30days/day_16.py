#!/bin/python3

import math
import os
import random
import re
import sys


def get_valid_string(string, min, max):
    if len(string) < min:
        return ""
    return string[:max]


if __name__ == '__main__':
    S = input()
    S = get_valid_string(S, 1, 6)
    try:
        AS
        print(int(S))
    except Exception as e:
        print("Bad String")
